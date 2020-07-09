# JANVI PANGORIYA SECTION-A ROLL NO -18
def bubble_sort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a
a = list(map(int,input("Enter the list that you want to sort : ").split()))
print("Sorted List :",bubble_sort(a))
