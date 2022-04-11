
a=[1,2,3,[4,5],[6,7,8,9]]
i=0
while i<len(a) :
    if type (a[i]) ==list:
        j=0
        while j<len(a[i]):
            print(i,j,a[i][j])
            j+=1
        i+=1
    else:
        print(i,a[i])
        i+=1
               