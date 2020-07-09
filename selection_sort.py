def selection_sort(a):
    for i in range(0,len(a)-1):
        mini=i
        for j in range(i+1,len(a)):
            if(a[j]<a[mini]):
                mini=j
        if(mini!=i):
            a[i],a[mini]=a[mini],a[i]
a = list(map(int,input("Enter the list to be sorted :").split()))
selection_sort(a)
print("Sorted List :",a)
