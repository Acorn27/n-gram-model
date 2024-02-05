from collections import defaultdict
from tokenizer import Tri_gram_Tokenizer

class Tri_gram():
    
    def __init__(self, smoothing_method = None, tokenizer = Tri_gram_Tokenizer):
        """
        Create tri gram language model.
        :param tokenizer: custom tokenizer depend on requiremnt
        :param smoothing_method: custom smoothing method depend on implementation
        """
        self.vocabublary = set()
        self.vocabublary_count = 0
        
        self.unigrams = defaultdict(dict)
        self.bigrams = defaultdict(dict)
        self.Tri_gram = defaultdict(dict)

        self.tokenizer = tokenizer
        self.smoothing_method = smoothing_method
    
    def fit(self, traning_data):
        """
        fit model probability according to training data
        :param traing_data: a list of training sentences
        """

        for sentence in traning_data:
            toks = self.tokenizer.tokenize(sentence)
            print(toks)
    
