class TrieNode:
        def __init__(self):
            self.children={}
            self.end_of_word=False
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        curr=self.root

        for i in word:
            if(i not in curr.children):
                curr.children[i]=TrieNode()
                print(childre)
            curr=curr.children[i]
            
        curr.end_of_word=True

    def insert_recursive(self,word):
        self.insert_recursive(self.root,word,0)

    def insert_recursive(self,curr,word,i):
        if(i==len(word)):
            curr.end_of_word=True
            return

        node=curr.children[word[i]]

        if(node is None):
            node=TrieNode()
            curr.children[word[i]]=node

        self.insert_recursive(node,word,i+1)

    def search(self,word):
        curr=self.root
        for i in word:
            node=curr.children[i]
            if(node is None):
                return False
            curr=node

        return curr.end_of_word

    def search_recursive(self,word):
        return self.search_recursive(self.root,word,0)

    def search_recursive(self,curr,word,i):
        if(i==len(word)):
            return curr.end_of_word
        
        node=curr.children[word[i]]
        if(node is None):
            return False

        return self.search_recursive(node,word,i+1)

    def delete(self,word):
        self.delete(self.root,word,0)
        
    def delete(curr,word,i):
        if(i==len(word)):
            #When end of word is reached only delete if curr.end_of_word is True
            if(curr.end_of_word is False):
                return False
            curr.end_of_word=False
            return len(curr.children)==0
        
        node=curr.children[word[i]]

        if(node is None):
            return False

        should_delete_current_node=delete(node,word,i+1)
        #If true is returned then delete the mapping of character and trienode reference from map.
        if(should_delete_current_node):
            curr.children.pop(word[i], None)
            #Return true if no mapping is left in the map
            return len(curr.children)==0
        return False
    
    def trie_words(self):
        curr=self.root
        words=[]
        self.helper("",curr,words)
        return words
    
    def helper(self,result,curr,words):
        print(result,curr,words)
        if(curr.end_of_word):
            words.append(result)
            return words
        while(curr.end_of_word is False):
            for child in curr.children:
                print(child)
                self.helper(result+child,curr.children[child],words)
                

def main():
    words=["abcd","dcba","lls","s","sssll"]
    trie=Trie()
    for word in words:
        trie.insert(word)
    trie.trie_words

main()
        



    

        

        

    
        
