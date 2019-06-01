from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
from typing import List, Optional, Dict, Tuple
from itertools import groupby


THEME_PRESENCE_THRESHOLD = 50


class InterestsExtractor:
    def __init__(self, tweets: Dict, word_to_theme_dict: Dict):
        self._tweets = tweets
        self._word_to_theme_dict = word_to_theme_dict

        self._mystem = Mystem()
        self._russian_stopwords = stopwords.words("russian")

        self._process_tweets()

    def print_result(self, prefix: str=""):
        if len(self.themes) == 0:
            print("{}No interests found".format(prefix))
            return
        for tup in self.themes:
            print("{}{:20}{:20}".format(prefix, tup[0], "-> {:.1f}%".format(tup[1])))

    @property
    def themes(self) -> List[Tuple[str, float]]:
        return self._themes

    def _process_tweets(self):
        all_themes = self._extract_themes()

        theme_counts = {theme: all_themes.count(theme) for theme in set(all_themes)}
        present_theme_counts = {
            t: c for t, c in theme_counts.items()
            if c >= THEME_PRESENCE_THRESHOLD
        }

        all_occurencies = sum([c for t, c in present_theme_counts.items()])
        if all_occurencies == 0:
            self._themes = []
            return

        present_themes = []
        for theme, count in sorted(present_theme_counts.items(), key=lambda item: item[1], reverse=True):
            percentage = 100 * count / all_occurencies
            present_themes.append((theme, percentage))

        self._themes = present_themes

    def _extract_themes(self) -> List[str]:
        all_themes = []
        for tweet_id, tweet in self._tweets.items():
            text = tweet["full_text"]
            themes = self._process_text(text)
            for theme in themes:
                all_themes.append(theme)
        return all_themes

    def _process_text(self, text: str) -> List[str]:
        words = self._preprocess_text(text).split(" ")

        themes = []
        for word in words:
            theme = self._get_theme_for_word(word)
            if theme:
                themes.append(theme)

        return themes

    def _preprocess_text(self, text: str) -> str:
        tokens = self._mystem.lemmatize(text.lower())
        tokens = [token for token in tokens if token not in self._russian_stopwords
                  and token != " "
                  and token.strip() not in punctuation]

        text = " ".join(tokens)

        return text

    def _get_theme_for_word(self, word: str) -> Optional[str]:
        if word in self._word_to_theme_dict:
            return self._word_to_theme_dict[word]
        return None
