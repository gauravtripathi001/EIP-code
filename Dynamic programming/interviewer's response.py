# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

Input: nums = [1,2,3]
Output:
dp =
 [
  []
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],

]

    
# single number I,II,III

# bit operation xor
#[1,2,3,9999,1,2,3]  find single copy of x in the vector.
    s=0 
    1^1 = 0
    2^2 = 0
    3^3 = 0
    x ^ 0 = x
    foreach i in vec:
        s ^=i
   return s

# [1,2,3,x,1,2,3,y] find one copy of elements x,y (x!=y)
# s = x^y  ==> find x,y
# s ! = 0

0011: x
0111: y
0100
 210
    s1[] bit2 is zero:  x
    s2[] bit2 is one:   y
# LSB(s)  {x,y} ==> {1,0};  {0, 1}
s=x^y
lsb=LSB(s) //give me one bit difference in x^y; pick the lowest bit
s1=0
s2=0
foreach i in vec:
    if (i & lsb) == lsb:
        s1 ^= i
    else:
        s2 ^= i
        
        s1 ==> x; s2 ==> y
        
        x+4+4 = x
        y+3+3 = y
    
   

# n=6, ["xyz", "123", "456", "@", "!", "abc"]


# https://codebunk.com/b/9231100130944/
print "Hello, world!"

# output: ["xyz","xyz123","xyz123456",...""]

#n=[1,2,3]
#convert_bits(len(n))-->000-->111
#create_all_bits(len(n))

#000-->[]
#001-->[1]
#010-->[2]
#100-->[3]
#101-->[1,3]
#110-->[2,3]
#111-->[1,2,3]

#for i in range(000,111):




