
class TrieNode():

    def __init__(self):
        self.childen = {}
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.childen:
                node.childen[char] = TrieNode()
            node = node.childen[char]
        node.is_end=True



    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node =self.root
        for char in word:
            if char not in node.childen:
                return False
            node =node.childen[char]
        return node.is_end


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        node =self.root
        for char in prefix:
            if char not in node.childen:
                return False
            node = node.childen[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)