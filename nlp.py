from statics import *

from spellchecker import SpellChecker

from nltk import ngrams, pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

from hazm.WordTokenizer import WordTokenizer
from hazm.SentenceTokenizer import SentenceTokenizer
from hazm import Stemmer
from parsivar import POSTagger
from hazm import Lemmatizer

import re



class Persian():

    def get_ngrams(self, document, order):
        content = self.clear_document(document)
        grams = ngrams(content.split(), order)
        result = []
        for item in grams:
            result.append(item)
        return result


    def get_dictionaries(self, document, which_dictionary):
        content = self.get_tokenized_words(document)
        output = []
        dictionary = ''
        if which_dictionary == 0:
            dictionary = PERSIAN_COMPUTER_DICTIONARY
        elif which_dictionary == 1:
            dictionary = PERSIAN_MEDICAL_DICTIONARY
        elif which_dictionary == 2:
            dictionary = PERSIAN_SPORT_DICTIONARY
        for item in content:
            if item in dictionary:
                output.append(item)
        return output 

    def clear_document(self, document):
        regex = re.compile('[^آ-ی]')
        content = regex.sub(' ', str(document))
        return content

    def split_document(self, content):
        words = content.split()
        result = ' '.join(sorted(set(words), key=words.index))
        result = result.split()
        return result


    def get_tokenized_words(self, document):
        ''' perisna tokenizer '''
        splited_content = self.clear_document(self.split_document(document))
        return WordTokenizer().tokenize(splited_content)

    def get_tokenized_sentence(self, document):
        ''' perisna tokenizer '''
        return SentenceTokenizer().tokenize(document)

    def get_pos_tag(self, document):
        tagger = POSTagger(tagging_model="wapiti")
        return tagger.parse(self.get_tokenized_words(document))


    def get_frequency(self, document):
        ''' remove repeated words and count '''
        content = self.clear_document(document)
        result = self.split_document(content)
        frequency = []
        for word in result:
            frequency.append([word, content.count(word)])
        return frequency



    def get_stemmer(self, document):
        ''' Stemmer '''
        content = self.clear_document(document)
        result = self.split_document(content)
        stemmer = Stemmer()
        word_stems = [(item, stemmer.stem(item)) for item in result]
        return word_stems



    def get_lemmatizer(self, document):
        ''' Lemmatizer '''
        content = self.clear_document(document)
        result = self.split_document(content)    
        lemmatizer = Lemmatizer()
        lemma_set = [(item, lemmatizer.lemmatize(item)) for item in result]
        return lemma_set


    def get_quotes(self, document):
        my_list = []
        all_quotes = re.findall('"([^"]*)"', document)
        for item in all_quotes:
            if item in PERSIAN_QUOTES:
                my_list.append(item)            
        my_list = list(dict.fromkeys(my_list))
        return my_list

    def get_alien_words(self, document):
        output = []
        content = self.get_tokenized_words(document)
        for item in content:
            for lang in ALIEN_WORDS:
                if item in lang:
                    output.append([item, ALIENS[ALIEN_WORDS.index(lang)]])
        return output







class English():

    def english_ngrams(self, document, order):
        content = self.clear_document(document)
        grams = ngrams(content.split(), order)
        output = []
        for item in grams:
            output.append(item)
        return output

    def clear_document(self, document):
        regex = re.compile('[^a-z A-Z]')
        content = regex.sub(' ', str(document))
        return content

    def split_document(self, content):
        words = content.split()
        result = ' '.join(sorted(set(words), key=words.index))
        result = result.split()
        return result



    def get_spellchecker(self, document):
        output = []
        spc = SpellChecker()
        tokenized_document = self.get_tokenized_words(document)
        for item in tokenized_document:
            checked = spc.correction(item)
            if item != checked:
                output.append([item, checked])
        return output

    def get_tokenized_words(self, document):
        ''' english tokenizer '''
        splited_content = self.clear_document(self.split_document(document))
        return word_tokenize(splited_content)

    def get_pos_tag(self, document):
        return pos_tag(self.get_tokenized_words(document))


    def get_dictionaries(self, document, which_dictionary):
        content = self.get_tokenized_words(document)
        output = []
        dictionary = ''
        if which_dictionary == 0:
            dictionary = ENGLISH_COMPUTER_DICTIONARY
        elif which_dictionary == 1:
            dictionary = ENGLISH_MEDICAL_DICTIONARY
        elif which_dictionary == 2:
            dictionary = ENGLISH_SPORT_DICTIONARY
        for item in content:
            if item in dictionary:
                output.append(item)
        return output



    def get_tokenized_sentence(self, document):
        ''' perisna tokenizer '''
        return sent_tokenize(document)


    def english_frequency(self, document):
        ''' remove repeated words and count '''
        content = self.clear_document(document)
        result = self.split_document(content)
        frequency = []
        for word in result:
            frequency.append([word, content.count(word)])
        return frequency



    def english_stemmer(self, document):
        ''' Stemmer '''
        content = self.clear_document(document)
        result = self.split_document(content)
        stemmer = PorterStemmer()
        word_stems = [(item, stemmer.stem(item)) for item in result]
        return word_stems



    def english_lemmatizer(self, document):
        ''' Lemmatizer '''
        content = self.clear_document(document)
        result = self.split_document(content)    
        lemmatizer = WordNetLemmatizer()
        lemma_set = [(item, lemmatizer.lemmatize(item)) for item in result]
        return lemma_set




# with open('../nlp1/fa_text.txt') as ff:
#     obj = Persian()
#     doc = ff.read()
#     print(obj.get_alien_words(doc))






