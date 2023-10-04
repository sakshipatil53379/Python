def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): # start from (10-1) which is 9 to 0 backword by 1 position
        for i in range(passnum): #start from zero till passnum
            print(alist)
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20,6]
bubbleSort(alist)
print(alist)

