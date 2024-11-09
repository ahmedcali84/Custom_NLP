import re
from NLP.tokenizer import *

class State:
    def __init__(self, is_final= False):
        self.transition = {}
        self.is_final = is_final
        self.output = ""

    def add_transition(self, char, state):
        self.transition[char] = state


class FST():
    def __init__(self):
        self.start_state = State()

    def add_word(self, word: str, lemma: str):
        current_state = self.start_state

        for character in word:
            if character not in current_state.transition:
                next_state = State()
                current_state.add_transition(char=character, state=next_state)
            else:
                next_state = current_state.transition[character]
            current_state = next_state

        current_state.is_final = True
        current_state.output = lemma

    def split_lemma_words(self, path: str):
        lines = []
        with open(path, "r") as f:
            for line in f:
                lines.append(line)

        # lines = lines[:151]
        for words in lines:
            pairs = [pair.strip() for pair in words.split("\t") if pair.strip()]
            if len(pairs) >= 1:
                lemma, word = pairs[0], pairs[1]
                # print(f"Adding: Lemma {lemma}, word {word}")
                self.add_word(word, lemma)

    def lemmatize(self, word: str) -> str:
        nouns = NLP("NLP/List of Proper Nouns.txt")
        pro_nouns = nouns.tokenize(punctuations=False)

        if re.match(r'\d+(th|st|nd|rd)$', word):
            return word[:-2]

        current_state = self.start_state
        for character in word:
            if character in current_state.transition:
                current_state = current_state.transition[character]
            else:
                for w in pro_nouns:
                    if w == word:
                        return w

        if current_state.is_final:
            return current_state.output
        else:
            return word
