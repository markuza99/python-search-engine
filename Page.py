from TrieNode import *

class Page:
    def __init__(self, index=None, words=None):
        self.index = index
        self.words = words
        self.trienode = TrieNode("*")
        for i in range(len(words)):
            add(self.trienode, words[i].lower(), i)
        self.indices = []
        self.references = 0
        self.references_found = 0



    def find_word(self, word):
        return search(self.trienode, word)

    def __str__(self):
        string = ""
        for position in self.indices:
            if position < 5:
                start = 0
            else:
                start = position - 5
            if start + 10 > len(self.words):
                stop = len(self.words)
            else:
                stop = start + 10
            for i in range(start, stop, 1):
                string += self.words[i] + " "
            string += "\n"

        return "Index:" + str(self.index) + "\nBroj ponavljanja reci: " + str(len(self.indices)) + "\nBroj linkova iz drugih dokumenata: " + str(self.references) + "\nBroj trazenih reci u linkovanim dokumentima: " + \
               str(self.references_found) + "\n\n" + string + "\n==========================================\n"


    def __lt__(self, other):
        return self.references + self.references_found + len(self.indices) > other.references + other.references_found + len(other.indices)



