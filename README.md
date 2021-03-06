# Filtering Tweets Using a Naive-Bayes Classifier 

The goal of this project is to use a Naive-Bayes Classifier to reduce the amount of tweets iFood's marketing team needs to read. They are mentioned in an enormous amount of tweets every single day, so it's hard for the marketing team to keep up with every tweet that they should give attention to. That's where this project comes in handy: It's able to automatically classify a specific tweet as **Relevant** or **Not Relevant**, which would help them a lot in keeping up with the tweets that actually matter.

The <a href="https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/">Naive-Bayes Classifier</a> works based on the Bayes' Theorem:

<div style="text-align: center;">
    <img src="https://latex.codecogs.com/gif.latex?P(A|B)=\frac&space;{P(B|A)&space;\cdot&space;P(A)}{P(B)}" title="P(A|B)=\frac {(P(B|A) \cdot P(A)}{P(B)}" />
</div>

In order to run the project a Twitter Developer Account had to be created. The account provides the keys needed to get tweets through <a href="http://docs.tweepy.org/en/latest/"><em>tweepy</em></a>. If you want to run the project locally, make sure to create a Developer Account and use your own keys. 

To know more details about the project refer to the RelevanceClassifier notebook. In order to run the project make sure to install all the libraries necessary with ```pip install -r requirements.txt```
