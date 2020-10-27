# Emotion_Sentiment_Analysis
Predict the sentiment of the text sentence 


The NRC Emotion Lexicon is a list of English words and their associations with eight basic emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two sentiments (negative and positive). The annotations were manually done by crowdsourcing.

The dataset is obtained from 
https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.html

The primary emotions are  'Positive', 'Negative', 'Anger','Anticipation','Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise','Trust' .

An input sentence or paragraph is broken down into individual tokens, the base word or the lemma of each token is obtained and it is compared with the words available in the dataset to get the emotion associated with that word.

The emotions are categorized as positive and negative emotions, a count of the occurence of each such emotion is kept and the overall sentiment of the sentence is given by the count of total positve and negative words occuring the sentence.

A Flask Web App is created of the same model.



