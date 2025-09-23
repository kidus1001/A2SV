# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie(object):

    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

    def insert(self, word):
        node = self
        for i in word:
            index = ord(i)-ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        node = self
        for i in word:
            index = ord(i) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_end
    
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        node = self
        for i in prefix:
            index = ord(i) - ord('a')
            if node.children[index] is None:
                return False
            else:
                node = node.children[index]
        return True
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)