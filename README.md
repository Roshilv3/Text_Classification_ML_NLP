# __TEXT CLASSIFICATION - SENTIMENT ANALYSIS__
### WorkFlow

1. Update config.yaml
2. Update params.yaml
3. Update entity file
4. Update Configuration file
5. Create Components
6. Create Pipeline
7. Update main.py
8. Create app.py


> Introduction of NLP

> Text Data Exploration and General Feature Extraction

> Flow of Project


### __Introduction to NLP__
#### Natural Language Processing (NLP)
Natural language processing strives to build machines that understand and respond to text or voice data—and respond with text or speech of their own—in much the same way humans do.
#### __What is natural language processing?__ 
Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.

NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to ‘understand’ its full meaning, complete with the speaker or writer’s intent and sentiment.

NLP drives computer programs that translate text from one language to another, respond to spoken commands, and summarize large volumes of text rapidly—even in real time. There’s a good chance you’ve interacted with NLP in the form of voice-operated GPS systems, digital assistants, speech-to-text dictation software, customer service chatbots, and other consumer conveniences. But NLP also plays a growing role in enterprise solutions that help streamline business operations, increase employee productivity, and simplify mission-critical business processes.

Source -IBM

#### Problem Statement
This Dataset is Download from Kaggle Website, [Click here](https://www.kaggle.com/datasets/mfaaris/spotify-app-reviews-2022) to know more about the dataset.
In this dataset we have an spotify app reviews in the google play store. We use the Reviews and trying to understand the Sentiment and gain more information from it. We will use the Text data which is available in the PlayStore. Some of the random reviews are taken from it and trying to analysing the sentiments.

Before that we annote the Rating (1,2=Negative,  3=Neutral,  4,5=Positive).

**Sentiment Analysis** is a process of computationally analyzing and identifying opinions and judgments from a piece of text. You can understand if a piece of text is positive, negative, or neutral, based on their sentiment analysis.

We use train test split to split the data from train and testing model. We use 80% of the data for training and ramaining 20% data for testing.

We use some of the machine learning model but before giving the data Vectorizing the text data using the CountVectorizer and TFIDF Vectorizer. After converting the data to the vectors, Fit the data to the various models such as LogisticRegresion, RandomForest and MultinomialNB. And at last we check the accuracy of the model and test the model with some random sentence.


### __Text Data Exploration and General Feature Extraction__
1. Reading The Data
2. Classifying the Ratings
4. __Preprocessing and Cleaning__
    - Clean Text
    - Remove Accented Words
    - Remove Stop Words
    - Word Lemmatization
5. __Feature Engineering__
    - Train-Test-Split
    - Text Encoding
        1. TF-IDF Vectorizer
6. __Model Classification__
    - LogisticRegression