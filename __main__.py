from InterestsExtractor import InterestsExtractor
from helpers import parse_tweets_for_user, parse_and_convert_themes_file


USERNAME = "yurydud"
THEMES_FILENAME = "theme_to_word.json"


if __name__ == "__main__":
    tweets = parse_tweets_for_user(USERNAME)
    word_to_theme_dict = parse_and_convert_themes_file(THEMES_FILENAME)
    ie = InterestsExtractor(tweets, word_to_theme_dict)
    print("Extracted interests for user '{}':".format(USERNAME))
    ie.print_result("\t")

