
class Tri_gram_Tokenizer():

    def _custom_preprocessing(self, sentence):
        """
        Special preprocessing to treat punctuation and ’s as seperate token
        :param sentence: inidividual string sentence
        :return: a processed string sentece
        """
        special_chars = ["’", '.', ',']
        chars = list(sentence)
        i = 0
        while i < len(chars):
            if chars[i] in special_chars:
                chars.insert(i, ' ')
                i += 2  # Skip the inserted space
            i += 1

        return ''.join(chars)


    def tokenize(self, sentence):

        """
        tokenize string sentence into tokens
        :param: string sentence
        :return: a list of tokens (or words) (inclued <s>'s and </s>)
        """
        refined_sentence = self._custom_preprocessing(sentence)

        augmented_sentence = "<s> " + "<s> " + refined_sentence + " </s>"

        return augmented_sentence.split()



