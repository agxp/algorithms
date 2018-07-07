class TrieNode:
    def __init__(self, character, end=False):
        self.children = {}
        self.end = end
        self.character = character

    def is_child(self, child):
        return child in self.children

    def child(self, character):
        return self.children[character]

    def add_child(self, character, end=False):
        if character not in self.children:
            self.children[character] = TrieNode(character, end)
        return self.children[character]

    def is_end(self):
        return self.end

    def get_children(self):
        return list(self.children)