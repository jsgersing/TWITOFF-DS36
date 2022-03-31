from sklearn.linear_model import LogisticRegression
from .models import User
import numpy as np
from .twitter import vectorize_tweet


def predict_user(user0_username, user1_username, hypo_tweet_text):

    # Query for the two users from the DB
    user0 = User.query.filter(User.username == user0_username).one()
    user1 = User.query.filter(User.username == user1_username).one()

    # Get the word embeddings from the user's tweets
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    # Combine their vectorization into a big X matrix
    X = np.vstack([user0_vects, user1_vects])

    # Create some 0's and 1's to generate a y vector
    # #(0's at the top, 1's at the bottom)
    y = np.concatenate([np.zeros(len(user0.tweets)),
                       np.ones(len(user1.tweets))])

    # Train our logistic regression

    # Get the word embedding for our hypothetical tweet
    # Make sure the word embedding is 2D
    # hypo_tweet_vect = np.array([vectorize_tweet(hypo_tweet_text)])

    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text)
    log_reg = LogisticRegression()
    log_reg.fit(X, y)

    # Generate a prediction
    # prediction = log_reg.predict(hypo_tweet_vect)

    # Return just the integer value from insdie of the prediction array
    # return prediction[0]
    return log_reg.predict(hypo_tweet_vect.reshape(1, -1))
