"""
This script is used to make submissions
"""


import logging

import hydra
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
from omegaconf.omegaconf import OmegaConf
from transformers import AutoTokenizer

from dataset import TextDataset

from models import (Attention_Pooling_Model,
                    Mean_Pooling_Model)


logger = logging.getLogger(__name__)

def create_dl(data_path, model_name, text_column, label_column):
    data = pd.read_csv(data_path)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    dataset = TextDataset(
        data[text_column].values, data[label_column].values, tokenizer, train=False
    )

    dataloader = DataLoader(dataset, batch_size=1, num_workers=4, pin_memory=True)

    return dataloader


def get_predictions(dataloader, model_type, model_path, model_name, dropout, num_labels, device):

    # set model architecture
    if model_type == "Attention_Pooling_Model":
        model = Attention_Pooling_Model(
            model_name, dropout, num_labels
        )

    elif model_type == "Mean_Pooling_Model":
        model = Mean_Pooling_Model(
            model_name, dropout, num_labels
        )

    else:
        raise RuntimeError("The provided model is not yet supported")

    model.load_state_dict(torch.load(model_path,map_location=device))
    model.to(device)

    pred = []
    for idx, inputs in enumerate(tqdm(dataloader)):

        input_ids = inputs["input_ids"].to(device, dtype=torch.long)
        attention_mask = inputs["attention_mask"].to(device, dtype=torch.long)
        outputs = model(input_ids, attention_mask)
        if num_labels<=1:
            pred.extend(torch.sigmoid(outputs).cpu().detach().numpy().tolist())
        #for multiclass 
        else:
            preds = outputs.argmax(dim=1)
            preds = preds.cpu().detach().numpy()
            pred.extend(preds)
    return pred


def save_preds(data_path, num_labels, preds, text_col_name, save_preds_path):

    if num_labels <=1:
        outputs = np.array(preds) >= 0.5
    else:
        outputs = preds
    data = pd.read_csv(data_path)
    if num_labels <=1:
        data = pd.DataFrame({'Text': data[text_col_name].values,
                          'Predicted Value': outputs.flatten() })
    else:
          data = pd.DataFrame({'Text': data[text_col_name].values,
                          'Predicted Value': outputs })

    data.to_csv(save_preds_path)



@hydra.main(config_path="./configs", config_name="config")
def main(cfg):
    logger.info(OmegaConf.to_yaml(cfg, resolve=True))
    dataloader = create_dl(
        cfg.dataset.test_data_path, cfg.model.model_name, 
        cfg.dataset.test_text, cfg.dataset.test_label
    )
    dropout=0
    preds = get_predictions(
        dataloader,
        cfg.model.model_type,
        cfg.dataset.finetuned_model_path,
        cfg.model.model_name,
        dropout,
        cfg.training.num_labels,
        device="cuda" if torch.cuda.is_available() else "cpu",
    )

    save_preds(cfg.test_data_path, cfg.training.num_labels, preds, cfg.dataset.test_text, cfg.dataset.save_preds_path)
    logger.info("Predictions saved in {}".format(cfg.dataset.save_preds_path))
if __name__ == "__main__":
    main()