from statics import PERSIAN_QUOTES, ALIEN_WORDS, ALIENS

from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

from hazm.WordTokenizer import WordTokenizer
from hazm import Stemmer
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

    def clear_document(self, document):
        regex = re.compile('[^آ-ی]')
        content = regex.sub(' ', str(document))
        return content

    def split_document(self, content):
        words = content.split()
        result = ' '.join(sorted(set(words), key=words.index))
        result = result.split()
        return result


    def get_tokenized(self, document):
        ''' perisna tokenizer '''
        content = self.clear_document(document)
        word_tokenizer = WordTokenizer()
        tokenized_content = word_tokenizer.tokenize(content)
        return tokenized_content

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
        content = self.get_tokenized(document)
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


    def english_tokenizer(self, document):
        ''' perisna tokenizer '''
        content = self.clear_document(document)
        tokenized_content = word_tokenize(content)
        return tokenized_content

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
















