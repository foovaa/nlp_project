import kivy
kivy.require('1.11.1')



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import escape_markup

import kivy.properties as kivyProps


import os
from nlp import Persian, English
import arabic_reshaper as ar
from bidi.algorithm import get_display



def display_persian(text):
    bidi_text = get_display(ar.reshape(text))
    return escape_markup(bidi_text)




Builder.load_file('main_kivy.kv')





class PagesScreenManager(ScreenManager):
    pass

class Wellcome(Screen):
    pass


class LoadDialog(FloatLayout):
    load = kivyProps.ObjectProperty(None)
    cancel = kivyProps.ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = kivyProps.ObjectProperty(None)
    cancel = kivyProps.ObjectProperty(None)
    text_input = kivyProps.ObjectProperty(None)




class EnglishPage(Screen):

    loadfile = kivyProps.ObjectProperty(None)
    savefile = kivyProps.ObjectProperty(None)
    text_input = kivyProps.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(EnglishPage, self).__init__(**kwargs)
        self.corpus = ''
        self.output = ''
        self.obj = English()
    
    '''
        Primary methods
    '''
    def tokenizeCorpus(self, flag):
        try:
            self.output = self.obj.get_tokenized_words(self.corpus) if flag else self.obj.get_tokenized_sentence(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            
    def tagCorpus(self):
        try:
            self.output = self.obj.get_pos_tag(self.corpus)
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')


            
    def spellCheckCorpus(self):
        try:
            self.output = self.obj.get_spellchecker(self.corpus)
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')


            
    def dictionaries(self, which_dictionary):
        try:
            self.output = self.obj.get_dictionaries(self.corpus, which_dictionary)
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')




    def lemmatizeCorpus(self):
        try:
            self.output =self.obj.english_lemmatizer(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            
    def stemmCorpus(self):
        try:
            self.output =self.obj.english_stemmer(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            

    def frequencyCorpus(self):
        try:
            self.output =self.obj.english_frequency(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            

    def ngramsCorpus(self, order):
        try:
            self.output =self.obj.english_ngrams(self.corpus, order)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            



    '''
        These methods are used for 
        1. Load corpus
        2. Implement UI windows
    '''

    def dismissPopup(self):
        self._popup.dismiss()

    def callLoadDialog(self):
        content = LoadDialog(load=self.load, cancel=self.dismissPopup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, filename):
        try:
            with open(os.path.join(filename[0])) as stream:
                self.corpus = self.text_input.text = stream.read()
                self.dismissPopup()
        except:
            self.dismissPopup()

    def nothingForNowPopup(self, title, message):
        showPopup(title, message)


    def callSaveDialog(self):
        content = SaveDialog(save=self.save, cancel=self.dismissPopup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        try:
            with open(os.path.join(path, filename), 'w') as stream:
                for item in self.output:
                    stream.write('%s\n'%str(item))
            self.dismissPopup()
            self.nothingForNowPopup('Output', 'Successful output saved!')
        except:
            self.dismissPopup()
            self.nothingForNowPopup('Output', 'Save output failed!')




class PersianPage(Screen):

    loadfile = kivyProps.ObjectProperty(None)
    savefile = kivyProps.ObjectProperty(None)
    text_input = kivyProps.ObjectProperty(None)
    is_persian = True

    def __init__(self, **kwargs):
        super(PersianPage, self).__init__(**kwargs)
        self.corpus = ''
        self.output = ''
        self.obj = Persian()
    '''
        Primary methods
    '''
    '''
        Primary methods
    '''
    def tokenizeCorpus(self, flag):
        try:
            self.output = self.obj.get_tokenized_words(self.corpus) if flag else self.obj.get_tokenized_sentence(self.corpus)         
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            

    def tagCorpus(self):
        try:
            self.output = self.obj.get_pos_tag(self.corpus)
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')


    def lemmatizeCorpus(self):
        try:
            self.output = self.obj.get_lemmatizer(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            
    def stemmCorpus(self):
        try:
            self.output = self.obj.get_stemmer(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            

            
    def dictionaries(self, which_dictionary):
        try:
            self.output = self.obj.get_dictionaries(self.corpus, which_dictionary)
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')


    def frequencyCorpus(self):
        try:
            self.output = self.obj.get_frequency(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            

    def ngramsCorpus(self, order):
        try:
            self.output = self.obj.get_ngrams(self.corpus, order)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            

    def quotesCorpus(self, order):
        try:
            self.output = self.obj.get_quotes(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            
            
    def aliensCorpus(self):
        try:
            self.output =self.obj.get_alien_words(self.corpus)        
            self.callSaveDialog()
        except:
            self.nothingForNowPopup('Tokenize', 'Error: Tokenizing failed!')
            


    '''
        These methods are used for 
        1. Load corpus
        2. Implement UI windows
    '''

    def dismissPopup(self):
        self._popup.dismiss()

    def callLoadDialog(self):
        content = LoadDialog(load=self.load, cancel=self.dismissPopup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, filename):
        with open(os.path.join(filename[0])) as stream:
            self.corpus = stream.read()
            self.text_input.text = self.corpus if not self.is_persian else display_persian(self.corpus)
        self.dismissPopup()

    def nothingForNowPopup(self, title, message):
        showPopup(title, message)


    def callSaveDialog(self):
        content = SaveDialog(save=self.save, cancel=self.dismissPopup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()



    def save(self, path, filename):
        try:
            with open(os.path.join(path, filename), 'w') as stream:
                for item in self.output:
                    stream.write('%s\n'%str(item))
            self.dismissPopup()
            self.nothingForNowPopup('Output', 'Successful output saved!')
        except:
            self.dismissPopup()
            self.nothingForNowPopup('Output', 'Save output failed!')







def showPopup(title, message):
    popupWindow = Popup(title=title, 
                        content=Label(text='[b]' + escape_markup(message) + '[/b]', markup=True),
                        size_hint=(None, None),
                        size=(400, 400))
    popupWindow.open()

class MyApp(App):
    def build(self):
        return PagesScreenManager()

if __name__ =='__main__':
    MyApp().run()