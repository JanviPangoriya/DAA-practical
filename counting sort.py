# JANVI PANGORIYA SECTION-A ROLL NO-18
def counting_sort(a,k):
    c=[]
    b=[]
    for g in range(len(a)):
        b.append(0)
    for i in range(0,k+1):
        c.append(0)
    for j in range(0,len(a)):
        c[a[j]]+=1
    for k in range(1,k+1):
        c[k]=c[k]+c[k-1]
    for l in range(len(a)-1,-1,-1):
        b[c[a[l]]-1]=a[l]
        c[a[l]]-=1
    return (b)
a = list(map(int,input(" Enter the array to be sorted").split()))
print("The sorted array :",counting_sort(a,max(a)))
