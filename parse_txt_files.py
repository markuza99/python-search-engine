import os
from Graph import *
from Page import *
from TrieNode import TrieNode
import re
pages = {}
g = Graph()
r = []

def read_results_from_files(root):
    filenames = os.listdir(root)
    result = {}
    for filename in filenames:
        content = read_results_from_file(os.path.join(root, filename)).decode('utf-8')
        words = content.split(' ')
        r.extend(words)
        try:
            page_number = int(content[:content.index('\n')].split()[-1])
        except:
            try:
                page_number = int(content[:content.index('\n')].split()[0])
            except:
                page_number = None
        index = filename.split(".")[0]
        result[index] = {'index': index,
                         'page_number': page_number,
                         'content': content}
        pages[index] = Page(index, words)
        g.add_vertex(index)
    connect_edges(result)
    return result

def connect_edges(dikt):
    for key, value in dikt.items():
        words = value["content"].split(" ")
        for i in range(len(words)-1):
            if "page" in words[i]:
                spliter = words[i+1]
                digit = "".join(re.findall('\d+', spliter))
                if len(digit) < 6:
                    for pagenum in range(770):
                        if str(digit) == str(pagenum):
                            for nk, nv in dikt.items():
                                if nv['page_number'] != None:
                                    if int(nv["page_number"]) == int(digit):
                                        g.add_edge(nk, key)



def read_results_from_file(path):
    with open(path, 'rb') as file:
        return file.read()

def logical_search_words(words):
    for page_path in pages:
        page_new = pages[page_path]
        for i in range(len(words)):
            if i == 0:
                page_new.indices = page_new.find_word(words[i])
            if words[i] == "AND":
                if i+1 < len(words):
                    new = page_new.find_word(words[i+1])
                    if len(page_new.indices) == 0:
                        page_new.indices = []
                    else:
                        if len(new) != 0:
                            page_new.indices += new
                        else:
                            page_new.indices = []
            elif words[i] == "OR":
                if i+1 < len(words):
                    new = page_new.find_word(words[i+1])
                    page_new.indices +=  new
            elif words[i] == "NOT":
                if i+1 < len(words):
                    new = page_new.find_word(words[i+1])
                    if len(new) != 0:
                        page_new.indices = []
            else:
                continue
            for link in g.incident_edges(page_new.index):
                page_new.references += 1
                page_new.references_found += len(pages[link].find_word(words[i]))





def search_words(words):
    for page_path in pages:
        page_new = pages[page_path]
        for i in range(len(words)):
            page_new.indices = page_new.find_word(words[i]) if i == 0 else page_new.indices + \
                                                                           page_new.find_word(words[i])
            for link in g.incident_edges(page_new.index):
                page_new.references += 1
                page_new.references_found += len(pages[link].find_word(words[i]))

if __name__ == '__main__':
    out_path = 'Data Structures and Algorithms in Python'
    results = read_results_from_files(out_path)
    print(g)
    while True:
        p = []
        y = ""
        bingo = input("\nUnesite rec za pretragu: ")
        words = bingo.split(" ")
        print(words)
        if "AND" in words:
            logical_search_words(words)
        elif "OR" in words:
            logical_search_words(words)
        elif "NOT" in words:
            logical_search_words(words)
        else:
            search_words(words)
        for page in sorted(pages.values()):
            if len(page.indices) != 0:
                p.append(page)
        start = 0
        finish = 5
        while start <= finish:
            if len(p) == 0:
                print("Pretraga ne odgovara ni jednoj stranici")
                break
            if start < len(p):
                print(p[start])
                start += 1
                if start == finish:
                    q = input("Da li zelite da predjete na drugu stranicu?")
                    if q.lower() == "da":
                        finish+= 5
                    else:
                        break
            if start == len(p):
                print("Stigli ste do poslednje stranice.")
                break


        izbor = input("Da li zelite da nastavite? (Da/Ne)")
        if izbor.lower() == "ne":
            break