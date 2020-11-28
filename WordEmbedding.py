import gensim
import pickle


class WordEmbedding:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format('corola.300.20.vec', binary=False,
                                                                     encoding='iso-8859-2')

    def get_similar_words(self, word):
        # word_vec = model.get_vector(word)
        similar_word = self.model.similar_by_word(word, topn=20)

        return similar_word

    @staticmethod
    def dump_vocabulary():
        keys = []

        with open('corola.300.20.vec', 'r', encoding='iso-8859-2') as rp:
            for line in rp.readlines():
                keys.append(str(line.split(' ')[0]))

        with open('vocabulary.txt', 'wb', encoding='iso-8859-2') as fp:
            pickle.dump(keys, fp)

    @staticmethod
    def load_vocabulary_into_trie(trie):
        with open('vocabulary.txt', 'rb', encoding='iso-8859-2') as fp:
            trie.insert_words(pickle.load(fp))

WordEmbedding.dump_vocabulary()