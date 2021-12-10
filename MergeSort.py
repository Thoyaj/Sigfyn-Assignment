#MergeSort
def MergeSort(arr):
    n=len(arr)
    if(n>1):
        mid=n//2        # mid of the array
        L=arr[:mid]     # first half
        R=arr[mid:]     # second half
        MergeSort(L)    # sorting first half
        MergeSort(R)    # sorting second half
        i=j=k=0
        while(i<len(L) and j<len(R)):  # Comparing elements and storing
            if(L[i]<R[j]):
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while(i<len(L)):        # Checking left out elements
            arr[k]=L[i]
            i+=1
            k+=1
        while(j<len(R)):
            arr[k]=R[j]
            j+=1
            k+=1
def PrintArr(arr):              # print array
    for i in range(len(arr)):
        print(arr[i], end=" ")

if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    MergeSort(arr)
    PrintArr(arr)
# Time Complexity: O(n*logn)
# Space Complexity: O(n)


