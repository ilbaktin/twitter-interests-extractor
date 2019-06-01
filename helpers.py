import json
from typing import Dict


def parse_tweets_for_user(username) -> Dict:
    with open("tweets/{}.json".format(username), "r") as f:
        data = json.load(f)
    return data["Tweets"]


def parse_and_convert_themes_file(filename) -> Dict:
    with open(filename, "r") as f:
        data = json.load(f)

    word_to_theme_dict = {}
    for theme, words in data.items():
        for word in words:
            word_to_theme_dict[word.lower()] = theme

    return word_to_theme_dict
