def binarySearch(lst,key):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(high+low)//2
        if (key==lst[mid]):
            print("elemnt found at",mid)
            return mid
        elif(lst[mid] > key):
            high=mid-1
        elif(lst[mid<key]):
            low=mid+1
    print("element not found")     
arr=[1,2,3,4,5,6,7,8,9,10]
print(binarySearch(arr,6))    
