class TrieNode(object):

    def __init__(self, char):
        self.char = char
        self.children = []
        self.indices = []


def add(father, word, i):
    node = father
    lower = word.lower()
    if lower.endswith("."):
        r = lower.split(".")
        lower = r[0]
    if lower.endswith(","):
        r = lower.split(",")
        lower = r[0]
    if lower.endswith(")"):
        r = lower.split(")")
        lower = r[0]
    if "www" in lower:
        r = lower.split(".")
        if len(lower) > 3:
            lower = r[1]
    if lower.startswith("("):
        r = lower.split("(")
        lower = r[1]
    if lower.endswith(":"):
        r = lower.split(":")
        lower = r[0]
    if lower.endswith(";"):
        r = lower.split(";")
        lower = r[0]

    for j in range(len(lower)):
        found_in_child = False

        for child in node.children:
            if child.char == lower[j]:
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(lower[j])
            node.children.append(new_node)
            node = new_node

    node.indices.append(i)


def search(root, word):
    node = root
    if not node.children:
        return []
    for i in range(len(word)):
        if len(word) == 0:
            return []
        char_not_found = True
        for child in node.children:
            if child.char == word[i]:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return []
    return node.indices
