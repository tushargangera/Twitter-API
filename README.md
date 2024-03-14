# Twitter Data Analysis Script

This script connects to Twitter API using Tweepy library to retrieve tweets from the home timeline and search for tweets with specific keywords. It also performs sentiment analysis on the retrieved tweets and translates Arabic text to English using the `translate` library.

## Requirements

- Python 3.x
- Tweepy library
- configparser library
- pandas library
- translate library

## Installation

1. Clone the repository:

```
git clone <repository_url>
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Create a `config.ini` file with your Twitter API keys and access tokens in the following format:

```
[twitter]
api_key = your_api_key
api_key_secret = your_api_key_secret
access_token = your_access_token
access_token_secret = your_access_token_secret
```

2. Run the script:

```
python script.py
```

## Functionality

- `getDataFromTwitter()`: Retrieves tweets from the home timeline and performs a keyword search. Prints retrieved tweets and saves them into DataFrames.
- `translate(str)`: Translates Arabic text to English. This function can be used to translate text provided as an argument.
- `stringFinder(text:str)`: Performs sentiment analysis on the input text. Prints whether the sentiment is positive, negative, or neutral.

## Example

```
# Running sentiment analysis on a negative text
stringFinder('Through the website, I opened an investment account, and I received a message from you, dear customer. The trading portfolio has been opened in the Saudi market No. ***, which is linked to your cash account No. ***. He called Al-Ahly Capital, saying, “Sorry, you do not have a trading portfolio.” 🙄😡')

# Running sentiment analysis on a positive text
stringFinder('thank you for the support')
```

Replace `<repository_url>` with the URL of your repository. This README.md provides users with information on how to use your script, its functionality, and how to set it up. You may want to expand or modify it according to your specific project requirements.
