class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        self.ancestor=None
        def helper(root):
            if(root==None):
                return
            results=[]
            if(root.left is not None):
                helper(root.left)
            if(root.right is not None):
                helper(root.right)
            dfs(root,results)
            if(p in results and q in results and self.ancestor is None):
                self.ancestor=root.val
        def dfs(node,results):
            if(node==None):
                return
            dfs(node.left,results)
            dfs(node.right,results)
            results.append(node.val)
        helper(root)
        return self.ancestor

class Solution_Optimized:
    def lowestCommonAncestor(self,root,p,q):
        self.ancestor=None
        def dfs(root,p,q,result):
            
            if(root is None):
                return
            if(root.left is not None):
                #l=dfs(root.left,p,q,result.copy())
                # if(l==root.left):
                #     return root.left
                dfs(root.left,p,q,result)
                
            if(root.right is not None):
                # r=dfs(root.right,p,q,result.copy())
                # if(r==root.right):
                #     return root.right
                dfs(root.right,p,q,result)
            print(root.val,result)    
            result.append(root.val)
            
            return result
                
            
        
        dfs(root,p,q,[])
        return self.ancestor

def main():
    results=[]
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.left.right.left=TreeNode(8)
    root.left.right.right=TreeNode(9)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(7)
    s=Solution_Optimized()
    print(s.lowestCommonAncestor(root,2,3))
    
main()
    
