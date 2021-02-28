import joblib, string, re
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class CheckMood:
    def __init__(self, text):
        self.text           = text    
        self.text_tokens    = word_tokenize(self.text)
        self.stop_words     = stopwords.words('english')

    def remove_noise(self):
        cleaned_tokens = []
        
        hyperlinks_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$_@.&+#-]|[!*\(\),]|"\
                                                            "(?:%[0-9a-zA-Z][0-9a-fA-F]+))")
        usrname_sym_regex = re.compile(r"(@[A-Za-z0-9_]+)")

        for token, tag in pos_tag(self.text_tokens):
            token = hyperlinks_regex.sub("", token)
            token = usrname_sym_regex.sub("", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'

            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in self.stop_words:
                cleaned_tokens.append(token.lower())

        model = joblib.load('media/models/sent_analysis_model_v1')

        feature = dict([token, True] for token in cleaned_tokens)

        return model.classify(feature)

