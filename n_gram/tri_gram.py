from collections import defaultdict
from tokenizer import Tri_gram_Tokenizer

import math

class Tri_gram():
    
    def __init__(self, use_smoothing = False, tokenizer = Tri_gram_Tokenizer()):
        """
        Create tri gram language model.
        :param tokenizer: custom tokenizer depend on requiremnt
        :param smoothing_method: custom smoothing method depend on implementation
        """
        self.vocabublary = set()
        self.vocabublary_count = 0
        self.is_trained = False
        
        self.uni_grams_count = defaultdict(int)
        self.bi_grams_count = defaultdict(int)
        self.tri_grams_count = defaultdict(int)

        self.tokenizer = tokenizer
        self.use_smoothing = use_smoothing
    
    def fit(self, traning_data):
        """
        fit model probability according to training data
        :param traing_data: a list of training sentences
        """

        # train with each sentence in training data
        for sentence in traning_data:
            toks = self.tokenizer.tokenize(sentence)
            self._update_probibility(toks)

            # since all sentence start with <s> <s>
            self.uni_grams_count["<s>"] += 1
            self.bi_grams_count[("<s>", "<s>")] += 1
        
        # update vocabublary
        self.vocabublary = set([key for key in self.uni_grams_count.keys()])
        self.vocabublary_count = len(self.vocabublary)
        self.is_trained = True
        
    
    def _update_probibility(self, toks):
        """
        Update n-gram count using list of tokens
        :param toks: list of tokens 
        :return: None (self + in-place update)
        """

        # skip the first 2 "<s>"
        for i in range(2, len(toks)):
            uni_gram = toks[i]
            bi_gram = (toks[i - 1], toks[i])
            tri_gram = (toks[i-2], toks[i-1], toks[i])

            self.uni_grams_count[uni_gram] += 1
            self.bi_grams_count[bi_gram] += 1
            self.tri_grams_count[tri_gram] += 1

    def get_ppl(self, test_sentence):
        """
        Predict the probability for a single test sentence
        :param test_sentence: a single test string
        :param use_smoothing: whether to use smoothing when compute probability
        :return: Predicted value for test sentence
        """

        if not self.is_trained:
            print("The model is not trained yet.")
            return

        
        toks = self.tokenizer.tokenize(test_sentence)
        probability = 0
        for i in range(2, len(toks)):
            try:
                raw_p = self._compute_P(toks[i], (toks[i-2], toks[i-1]))
            except Exception as e:
                return e
            log_p = math.log2(raw_p)
            probability += log_p
        x = (-1 / (len(toks) - 2))
        return 2 ** x
        

    def _compute_P(self, hypothesis, given):
        """
        Compute probability of "hypothesis" | "given"
        :param hypothesis: a word at which we want to compute probability
        :param given: the trigram context for hypothesis, which is the previous 2 words
        """
        count_hypothesis = (given[0], given[1], hypothesis)
        count_give = (given)
        # print(given)
        # print(f"{' '.join((given[0], given[1], hypothesis))}")

        numerator = self.tri_grams_count[count_hypothesis]
        denominator = self.bi_grams_count[count_give]

        # print(denominator)
        # print(numerator)

        if self.use_smoothing:
            if denominator == 0:
                for key in self.bi_grams_count.keys():
                    self.bi_grams_count[key] += 1
                self.bi_grams_count[given] = 1
                denominator = 1

            if numerator == 0:
                for key in self.tri_grams_count.keys():
                    self.tri_grams_count[key] += 1
                self.tri_grams_count[count_hypothesis] = 1
                numerator = 1


        if denominator == 0:
            raise Exception(f"Never seen bi-gram '{' '.join(given)}' before")
        elif numerator == 0:
            raise Exception(f"Never seen tri-gram '{' '.join((given[0], given[1], hypothesis))}' before")
        else:
            return numerator / denominator

    def info(self):
        """
        Print out uni-gram, bi-gram, tri-gram count after fit training data
        :return: None
        """

        # error check
        if not self.is_trained:
            print("The model is not trained yet.")
            return


        print("Uni-gram count:")
        for word, count in sorted(self.uni_grams_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{count}\t\t{word}")
        
        print("Bi-gram count:")
        for word, count in sorted(self.bi_grams_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{count}\t\t{word}")
        
        print("Tri-gram count:")
        for word, count in sorted(self.tri_grams_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{count}\t\t{word}")

    
