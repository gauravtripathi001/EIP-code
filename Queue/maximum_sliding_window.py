import collections
def max_in_sliding_window(arr, w):
    deque=collections.deque()
    res=[]
    
    for i in range(len(arr)):
        
        while(len(deque)>0 and arr[i]>=arr[deque[-1]]):
            deque.pop()
        deque.append(i)
        
        if(i-w+1>=0):
            if(deque[0]<=i-w):
                deque.popleft()
            res.append(arr[deque[0]])
    return res

def main():
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    w = 3
    print(max_in_sliding_window(arr, w))
    
main()
