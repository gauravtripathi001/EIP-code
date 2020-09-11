def edit_distance_bf(s1,s2):
    l1=len(s1);l2=len(s2)

    if(l1==0):
        return l2
    if(l2==0):
        return l1

    if(s1[0]==s2[0]):
        return edit_distance_bf(s1[1:],s2[1:])

    return 1+min(edit_distance_bf(s1[1:],s2[1:]),
               edit_distance_bf(s1,s2[1:]),
               edit_distance_bf(s1[1:],s2)
               )

def main():
    s1="cat"
    s2="bat"
    print(edit_distance_bf(s1,s2))

main()
