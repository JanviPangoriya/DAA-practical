def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
l= list(map(int,input("enter the list to be sorted:").split()))
insertionSort(l)
print("Sorted list :",l)
