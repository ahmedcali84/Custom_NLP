from NLP.tokenizer import *
from NLP.lemmitizer import *
import unittest

class TestNLPMethods(unittest.TestCase):
    def setUp(self):
        self.nlp = NLP("test/pg74494.txt")
        self.stop = NLP("test/stopwords.txt")
        self.fst = FST()
        self.fst.split_lemma_words("test/lemmatization-en.txt")

    def test_data_path(self):
        self.assertIn("File_Path", self.nlp.data_path())

    def test_read_chars(self):
        self.assertIsInstance(self.nlp.read_chars(100), str)

    def test_tokenize(self):
        tokens = self.nlp.tokenize()
        self.assertGreater(len(tokens), 0)

    def test_lemmatize_1(self):
        lemma = self.fst.lemmatize("first")
        print(f"Word: 1, Lemma: {lemma}")
        self.assertNotEqual(lemma, "LEMMA NOT FOUND")
    
    def test_lemmatize_2(self):
        lemma = self.fst.lemmatize("hundredth")
        print(f"Word: 100, Lemma: {lemma}")
        self.assertNotEqual(lemma, "LEMMA NOT FOUND")
        
    def test_lemmatize_3(self):
        lemma = self.fst.lemmatize("abdomina")
        print(f"Word: abdomina, Lemma: {lemma}")
        self.assertNotEqual(lemma, "LEMMA NOT FOUND")
        
    def test_lemmatize_4(self):
        lemma = self.fst.lemmatize("playing")
        print(f"Word: playing, Lemma: {lemma}")
        self.assertNotEqual(lemma, "LEMMA NOT FOUND")
        
    def test_lemmatize_tokens(self):
        tokens = self.nlp.tokenize()
        stop = self.stop.tokenize()
        tokens = [word for word in tokens if word not in stop]
        # print([token for token in tokens])
        for token in tokens:
            lemma = self.fst.lemmatize(token)
            print(f"Word: {token}, Lemma: {lemma}")
            self.assertNotEqual(lemma, "LEMMA NOT FOUND", f"Expected lemma for '{token}' was not found.")

if __name__ == '__main__':
    unittest.main()

