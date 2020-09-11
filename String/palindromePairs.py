class Solution:
    def palindromePairs(self, words):
        class Node:
            def __init__(self):
                self.children={}
                self.idx=0
                self.is_word=False
        
        #Insert a word in trie
        def insert(root,i,word):
            curr=root
            for c in word:
                if(c not in curr.children):
                    curr.children[c]=Node()
                curr=curr.children[c]
            curr.is_word=True
            curr.idx=i
        
        #build trie with words
        def build_trie(words):
            root=Node()
            for i,word in enumerate(words):
                insert(root,i,word)
            return root
        
        root1=build_trie(words)
        curr=root1
        result=set()
        
        for idx,word in enumerate(words):
            r_word=word[::-1];l=len(r_word);
            for i,c in enumerate(r_word):
                if(c not in curr.children):
                    break
                else:
                    curr=curr.children[c]
                    if(curr.is_word):
                        if(i==l-1):
                            result.add((curr.idx,idx))
                        else:
                            if(is_palindrome(r_word[i+1:])):
                                result.add((curr.idx,idx))
        #return result
        #output = [list(elem) for elem in result]
        #return output

        def printTrie(root):
            curr=root
            while(curr.):
                for child in curr.children:
                    
        def helper():
        
def main():
    words=["abcd","dcba","lls","s","sssll"]
    sol=Solution()
    print(sol.palindromePairs(words))

main()
