def linearSearch(lst,key):
    for i  in lst:
        if(i == key):
            print("elemnt found at ", i)
            return i
arr=[224,98,2,3,5,8,10,36]
linearSearch(arr,8)