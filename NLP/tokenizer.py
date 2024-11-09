import numpy as np
from collections import Counter
import os
import re

class NLP:
    def __init__(self, data: str):
        if os.path.exists(data):
            self.data = data
        else:
            raise FileNotFoundError(f"Error: File {data} Does Not Exist. Provide Correct File Path.")

    def data_path(self) -> str:
        """
        returns the name/filepath of the document
        """
        file_size = os.path.getsize(self.data) / (1024**2)
        return f"File_Path: {self.data}, File Size: {file_size:.2f} MB"

    def _read_file(self) -> str:
        try:
            with open(self.data, "r", encoding="utf-8-sig") as f:
                return f.read()
        except Exception as e:
            print(f'Error: {e}')
            return None

    def read_chars(self, chars_len: int =None) -> str:
        """ returns the first chars_len of the document else
        whole if no parameter for the length is provided
        """
        if chars_len is not None and chars_len < 0:
            raise ValueError("Error: chars_len must be a non-negative int number")
        data = self._read_file()
        if data is None:
            return ''
        return data if chars_len is None else data[:chars_len]

    def read_lines(self,lines_length:int) -> list:
        '''
        prints the specified number of lines from the file
        '''
        if isinstance(lines_length, int):
            data = self.__read_file()
            if data is None:
                return []
            lines = data.splitlines()
            return [lines[i].strip() for i in range(min(lines_length, len(lines)))]
        else:
            print("Length Specified Must be of type int")
            return None

    def tokenize(self, punctuations: bool =True) -> list:
        """
        Returns words in the file as a list.
        Returns an empty list if no words are found or if there is an error reading the file.
        """
        remove_words = "()[]{}$@&|#.,*&^%!<>?/\\+~`_\":=;\t"
        data = self.read_chars()
        if data is  None:
            return []
        lower = data.lower()
        if punctuations == True:
            # Removing remove words
            remove_r_w = lower.translate({ord(i): None for i in remove_words })
            # Removing Hyphens
            remove_hyphen = re.sub(r'-', ' ', remove_r_w)
            # removing th from numbers
            remove_r_w = re.sub(r'\d+(st|nd|rd|th)$', lambda m: m.group(0)[:-2], remove_r_w)
            # Removing apostrophes
            apostrophe_removal = re.sub(r'\b(\w+)-(\w+)\b', r'\1 \2', remove_hyphen)
            apostrophe_removal = re.sub(r"\b(\w+)'ll\b", r"\1 will", apostrophe_removal)  # "I'll" -> "I will"
            apostrophe_removal = re.sub(r"\b(\w+)'ve\b", r"\1 have", apostrophe_removal)  # "I've" -> "I have"
            apostrophe_removal = re.sub(r"\b(\w+)'re\b", r"\1 are", apostrophe_removal)   # "You're" -> "You are"
            apostrophe_removal = re.sub(r"\b(\w+)'d\b", r"\1 would", apostrophe_removal)  # "I'd" -> "I would"
            apostrophe_removal = re.sub(r"\b(\w+)'m\b", r"\1 am", apostrophe_removal)     # "I'm" -> "I am"
            apostrophe_removal = re.sub(r"\b(\w+)'s\b", r"\1", apostrophe_removal)        # Remove possessive: "John's" -> "John"
            apostrophe_removal = re.sub(r"\b(\w+)'t\b", r"\1 not", apostrophe_removal)    # "isn't" -> "is not", "won't" -> "will not"
            # Handle contractions with "n't"
            apostrophe_removal = re.sub(r"\b(can)'t\b", r"\1 not", apostrophe_removal)    # "can't" -> "cannot"
            apostrophe_removal = re.sub(r"\b(won)'t\b", r"\1 will not", apostrophe_removal)  # "won't" -> "will not"
            apostrophe_removal = re.sub(r"\b(shan)'t\b", r"\1 shall not", apostrophe_removal) # "shan't" -> "shall not"
            # Handle special cases like "'tis" or "'twas"
            apostrophe_removal = re.sub(r"\b'tis\b", "it is", apostrophe_removal)         # "'tis" -> "it is"
            apostrophe_removal = re.sub(r"\b'twas\b", "it was", apostrophe_removal)       # "'twas" -> "it was"
            # Split on New Line Characters
            clean = " ".join(apostrophe_removal.split('\n')).split(" ")
            cleaned = [word for word in clean if word]
            return cleaned

        elif punctuations == False:
            clean = " ".join(lower.split('\n')).split(" ")
            cleaned = [word for word in clean if word]
            return cleaned

    def bag_of_words(self) -> dict:
        """
        returns Bag of words, (word and its count as dict)
        """
        data = self.tokenize()
        counter = Counter(data)
        return dict(counter)

    def sort_bag_of_words(self, by: str = "value") -> dict:
        """
        Returns sorted bag of words by value if True and by keys if False.
        Returns sorted bag of words by value by Default.
        """
        if by == "value":
            sorted_bow = dict(sorted(self.bag_of_words().items(), key=lambda item: item[1], reverse=True))
            return sorted_bow
        elif by == "key":
            sorted_bow = dict(sorted(self.bag_of_words().items(), key=lambda item: item[0], reverse=False))
            return sorted_bow
        else:
            raise ValueError("ERROR: Invalid Sort Parameter, by parameters must be 'key' or 'value'")
