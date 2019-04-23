import nltk
from nltk.tokenize import word_tokenize
import unidecode
import string

class Normalizador:

	def __init__(self):
		self.sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
		self.word_tokenizer = word_tokenize
		self.stemmer = nltk.stem.RSLPStemmer() 
		self.lemmatizer = "I am a fucking Portuguese Lemmatizer!"

	def remove_accents(self, text):
		return unidecode.unidecode(text)

	def remove_punctuation(self, text):
	    return text.translate(str.maketrans('', '', string.punctuation))

	def tokenize_sentences(self, text):
	    sentences = self.sent_tokenizer.tokenize(text)
	    return sentences

	def tokenize_words(self, text):
	    tokens = self.word_tokenizer(text)
	    return tokens

	def lemmatize(self, text):
	    return lemmatizer

	def stemmize(self, tokens):
		stemized_words = []
		
		for word in tokens:
			stemized_words.append(self.stemmer.stem(word))

		return stemized_words

	def normalization_pipeline(self, text, remove_accents=False, remove_punctuation=False, 
		tokenize_sentences=False, tokenize_words=False, lemmatize=False, stemmize=False):

	    text = self.remove_accents(text) if remove_accents else text
	    text = self.remove_punctuation(text) if remove_punctuation else text
	    text = self.tokenize_sentences(text) if tokenize_sentences else text
	    text = self.tokenize_words(text) if tokenize_words else text
	    text = self.lemmatize(text) if lemmatize else text
	    text = self.stemmize(text) if stemmize else text
	    
	    return text