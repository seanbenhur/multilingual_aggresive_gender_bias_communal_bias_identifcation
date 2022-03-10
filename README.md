# Hypers at ComMA@ICON: Modelling Aggressiveness, Gender Bias and Communal Bias Identification

## Overview
This is the official github repository for the solution for ComMA@ICON 2021 Shared task on Multilingual  Gender Biased and Communal Language Identification. Our methodology was able to Rank 2, Rank 3, Rank 4, Rank 5 on Multilingual , Bengali, Meitei and Hindi.


## Abstract
Due to the exponentially increasing reach of social media, it is essential to focus on its negative aspects as it can potentially divide society and incite people into violence. In this paper, we present our system description of work on the shared task ComMA@ICON, where we have to classify how aggressive the sentence is and if the sentence is gender-biased or communal-biased.These three could be the primary reasons to cause significant problems in society. As team Hypers we have proposed an approach which utilizes different pretrained models with Attention and mean pooling methods. We were able to get Rank 3 with 0.223 Instance F1 score on Bengali, Rank 2 with 0.322 Instance F1 score on Multi-lingual set, Rank 4 with 0.129 Instance F1 score on Meitei and Rank 5 with 0.336 Instance F1 score on Hindi. The source code and the pretrained models of this work can be found here1.

## Model Weights with better results
After the publication, we found using  XLM-Align-Base model improves the results further without using Attention/Mean Pooling, The model weights will be avilable in the huggingface hub


## Tak Overview
Aggression and its manifestations in different forms have taken unprecedented proportions with the tremendous growth of Internet and social media. The research community, especially within the fields of Linguistics and Natural Language Processing, has responded by understanding the pragmatic and structural aspects of such forms of language usage ((Culpeper, 2011; Hardaker, 2010, 2013) and several other) and developing systems that could automatically detect and handle these ((Kumar et al., 2018; Zampieri et al., 2019; Waseem et al., 2017; Nobata et al., 2016; Dadvar et al., 2013) and numerous others).

In the ComMA project, we are working on these different aspects of aggressive and offensive language usage online and its automatic identification. As part of our efforts in the project, we present a novel multi-label classification task to the research community, in which each sample will be required to be classified as aggressive, gender biased or communally charged. We expect that the task will be interesting for researchers working in the different related areas of hate speech, offensive language, abusive language as well more generally in text classification.


1.Sub-task A: Aggression Identification. The task will be to develop a classifier that could make a 3-way classification in between ‘Overtly Aggressive’(OAG), ‘Covertly Aggressive’(CAG) and ‘Non-aggressive’(NAG) text data.

2.Sub-task B: Gender Bias Identification. This task will be to develop a binary classifier for classifying the text as ‘gendered’(GEN) or ‘non-gendered’(NGEN).

3.Sub-task C: Communal Bias Identification: This task will be to develop a binary classifier for classifying the text as ‘communal' (COM) and 'non-communal'(NCOM).

The task could be approached as three separate classification tasks or a multi-label classification task or a structured classification task.


## Data

Refer [data.md](https://github.com/seanbenhur/multilingual_aggresive_gender_bias_communal_bias_identifcation/blob/main/data/README.md) for more details

## Results

Results of various





