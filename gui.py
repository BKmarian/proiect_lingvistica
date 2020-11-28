import tkinter as tk
from tkinter import *

from WordEmbedding import WordEmbedding
from levenstein import levenshtein
from trie import Trie

trie_fst = Trie()
WordEmbedding.load_vocabulary_into_trie(trie_fst)
word_emb = WordEmbedding()

def correct(event):
    words = area.get("1.0", END).split()
    false_words = [word for word in words if trie_fst.find_word(word) is False]
    print(false_words)
    #true_words = [word for word in words if trie_fst.find_word(word) == True]
    sims = {word: get_similarity(word) for word in false_words}
    print(sims)


def get_similarity(word):
    return [(ws, levenshtein(ws, word)) for ws in word_emb.get_similar_words(word)].sort(key=lambda x: x[1])[:5]


root = tk.Tk()
area = tk.Text(root, height=40, width=60)
area.pack()

widget = tk.Button(text="Correct")
widget.bind('<Button-1>', correct)
widget.place(anchor=S, height=20, width=20)
widget.pack()

tk.mainloop()
