# TWITOFF-DS36: Who Tweeted It?

This is the repository for a BloomTech project for which I built a Flask app, extracted data from the Twitter API, used that data to train a Logistic Regression Model, wrote some basic html files to display model's prediction, and deployed the app to Heroku. 

## Introduction

The goal of this project was a proof-of-concept: Can we connect to Twitter's API, use Twitter data to train a LR model, which -- when given a user generated tweet -- will predict which of two Twitter users (also chosen by the user) was more likely to have tweeted it.


### Data extraction

####  Twitter API 
First, you'll need a Twitter account. If you don't already have one, it's quick and easy to sign up. You'll then need to apply for developer access: https://developer.twitter.com/en/apply-for-access . Depending on your needs, you can apply for "ELEVATED" status, which allows you to pull up to 2,000,000 tweets per month. Create a Project and then create a Development App. 

#### Twitter Credentials Storage and Access

Now that we have an app, we can get a Twitter API Key and Secret (like a username and password) for the app, as they will be required to authenticate with the Twitter web API for our application. For security, it is best practice to keep these credentials in a file. For this projects, they are in a .env file, which is included in a .gitignore file. 

### Deployment

In order to access the final version of the app, please visit the following link: https://twitoff-js-ds36.herokuapp.com/

## Repo Structure
```
│
├── .vscode                      <- Linter added.
├── My_model                     <- Vectorizer for converting text to numbers
│   ├── attribute_rule               
│   ├── lemmetizer/lookups           
│   ├── ner                          
│   ├── parser
│   ├── senter                       
│   ├── tagger
│   ├── tok2vsc
│   ├── vocab
│   ├── config.cfg
│   ├── meta.json
│   └── tokenizer
│    
├── twitoff                      <- Internal folder 
│   ├──templates                 <- html templates folder
│   │    ├── base.html           <- Homepage
│   │    ├── prediction.html     <- Page where prediction is revealed
│   │    └── user.html           <- Page to display users and tweets
│   ├── __init__.py
│   ├── app.py
│   ├── db.sqlite.py             <- Sqlite3 database
│   ├── models.py                <- Create and connect to the Database
│   ├── predict.py               <- Training the Logistic Regression model
│   └── twitter.py               <- Authentic and connect with API
├── .gitignore                   <- Items not to be pushed to Github
├── Pipfile                      <- Necessary packages
├── Pipfile.lock                  
├── Procfile                     <- Needed to deploy to Heroku
└── README.md                    <- For interested developers 
```