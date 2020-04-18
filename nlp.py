from statics import PERSIAN_QUOTES, ALIEN_WORDS, ALIENS

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
        content = self.clear_document(document)
        return WordTokenizer().tokenize(content)

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


    def get_tokenized_words(self, document):
        ''' perisna tokenizer '''
        content = self.clear_document(document)
        tokenized_content = word_tokenize(content)
        return tokenized_content

    def get_pos_tag(self, document):
        return pos_tag(self.get_tokenized_words(document))


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




# test = '''
# هدف اصلي در پردازش زبان طبيعي، ايجاد تئوري‌هاي محاسباتي از زبان، با استفاده از الگوريتم‌ها و ساختارهاي داده‌اي موجود در علوم رايانه‌اي است. بديهي است كه در راستاي تحقق اين هدف، نياز به دانشي وسيع از زبان است و علاوه بر محققان علوم رايانه‌اي، نياز به دانش زبان شناسان نيز در اين حوزه مي‌‌باشد. كاربردهاي پردازش زبان طبيعي به دو دسته كلي قابل تقسيم است: كاربردهاي نوشتاري و كاربردهاي گفتاري. از كاربردهاي نوشتاري آن مي توان به استخراج اطلاعاتي خاص از يك متن، ترجمه يك متن به زباني ديگر و يا يافتن مستنداتي خاص در يك پايگاه داده نوشتاري (مثلا يافتن كتاب‌هاي مرتبط به هم در يك كتابخانه) اشاره كرد. نمونه‌هايي از كاربردهاي گفتاري پردازش زبان عبارتند از: سيستم‌هاي پرسش و پاسخ انسان با رايانه، سرويس‌هاي اتوماتيك ارتباط با مشتري از طريق تلفن و يا سيستم هاي كنترلي توسط صدا. در سال‌هاي اخير اين حوزه تحقيقاتي توجه دانشمندان را به خود جلب كرده است و تحقيقات قابل ملاحظه‌اي در اين زمينه صورت گرفته است.

# پردازش زبان طبيعي يکي از زيرشاخه‌هاي با اهميت در حوزه گسترده هوش مصنوعي و دانش زبان‌شناسي‌ است. تلاش عمده در اين زمينه، ماشيني کردن فرايند درک و برداشت مفاهيم بيان شده توسط يک زبان طبيعي انساني است. به تعريف دقيقتر پردازش زبان هاي طبيعي عبارت است از استفاده از رايانه به منظور پردازش زبان گفتاري و نوشتاري. پردازش زبان ها و مکالمات طبيعي يکي از اموري است که با ورود فناوري رايانه اي به زندگي بشر مورد توجه بسياري از دانشمندان قرار گرفته است. حتي انديشه‏‌اي که تورينگ از ماشين هوشمند خود و تعريفي که او از هوش مصنوعي داشت، در مرحله اول مربوط به پردازش زبان طبيعي ميشد.

# به تعريف دقيق‌تر پردازش زبان‌هاي طبيعي عبارت است از استفاده از رايانه براي پردازش زبان گفتاري و نوشتاري. با استفاده از آن مي‌توان به ترجمه زبان‌ها پرداخت، از صفحات وب و بانک‌هاي اطلاعاتي نوشتاري جهت پاسخ دادن به پرسش‌ها استفاده کرد، يا با دستگاه‌ها (مثلاً براي مشورت گرفتن) به گفتگو پرداخت.

# پردازش زبان طبيعي چيست؟

# پردازش زبان‌هاي طبيعي زيرشاخه‌اي از هوش مصنوعي است که با توسعه و استفاده از مدل‌هاي رايانشي براي پردازش زبان سر و کار دارد. در اين زمينه، دو حيطه اصلي پژوهش وجود دارد: ادراک، که با فرايندهايي سر و کار دارد که اطلاعات را از زبان استخراج مي‌کنند (مانند درک زبان طبيعي، بازيابي اطلاعات) و توليد، که با فرايندهايي سر و کار دارد که با استفاده از زبان به انتقال اطلاعات مي‌پردازند. معمولاً کارهاي مرتبط با گفتار را تحت عناوين جداگانه تشخيص گفتار و توليد گفتار قرار مي‌دهند.

# با اينکه مجموعه گسترده‌اي از روش‌ها در پردازش زبان طبيعي بکار مي‌روند، تکنيک‌هاي بکار رفته را مي‌توان به سه دست? کلي تقسيم نمود: روش‌هاي آماري، روش‌هاي ساختاري/مبتني بر الگو و روش‌هاي مبتني بر استنتاج. بايد توجه داشت که اين راهکارها لزوماً از هم جدا نيستند. در واقع، جامع‌ترين مدل‌ها از ترکيب هر س? اين روش‌ها استفاده مي‌کنند. تفاوت اين راهکارها در نوع عمليات پردازشي است که قادر به انجام آن هستند و ميزان قواعدي که در مقابل آموزش/يادگيري خودکار از روي داده‌هاي زباني نياز دارند.
# سطوح تحليل زباني:

#     آواشناسي/واج‌شناسي
#     ساختواژه (صرف)
#     نحو
#     معني‌شناسي
#     کاربردشناسي
#     گفتمان
# '''

# obj = Persian()
# print(obj.get_pos_tag(test))











