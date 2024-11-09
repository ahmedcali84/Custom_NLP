# Custom NLP Library

This **NLP class** handles file-based text processing, including reading, tokenizing, and creating a sorted bag of words. It supports detailed cleaning steps to normalize contractions, hyphens, and punctuation for accurate analysis.

The **Lemmatize class** applies a `finite state transducer (FST)` model to systematically break down words and reduce them to their *lemmas* by following character transitions. It uses a trie structure to store transitions between characters and determine if a word matches a stored lemma, enhancing accuracy by filtering out proper nouns through the *NLP.tokenizer*.

## Dependencies
- *numpy*

## Install Dependencies

```bash
pip install numpy
```

## Run Tests
***Clone the Repository and run:***

``` bash
python run_tests.py
```
