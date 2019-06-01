from InterestsExtractor import InterestsExtractor
from helpers import parse_tweets_for_user, parse_and_convert_themes_file


USERNAMES = ["yurydud", "yurydud", "yurydud"]
THEMES_FILENAME = "theme_to_word.json"


if __name__ == "__main__":
    for username in USERNAMES:
        tweets = parse_tweets_for_user(username)
        word_to_theme_dict = parse_and_convert_themes_file(THEMES_FILENAME)
        ie = InterestsExtractor(tweets, word_to_theme_dict)
        print("Extracted interests for user '{}':".format(username))
        ie.print_result("\t")

