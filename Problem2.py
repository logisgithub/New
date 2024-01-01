def findCombination(dieA,dieB):
    combinations=[]
    for i in range(len(dieA)):
        for j in range(len(dieB)):
            li=[]
            li.append(dieA[i])
            li.append(dieB[j])
            combinations.append(tuple(li))
    return combinations

def arraySum(arr):
    c=0
    for i in range(len(arr)):
        c+=arr[i]
    return c

def find(array,n,co):
    count=0
    for i in range(len(array)):
        if arraySum(array[i])==co:
            count+=1
            if count>n:
                return 0
    if count!=n:
        return 0
    else:
        return 1

def changeValue(DiceA,DiceB):
    for i in range(1,len(DiceB)-1):
        if DiceB[i]==8:
            DiceB=[1,2,3,4,5,8]
            return changeValueDieA(DiceA,DiceB)
    return changeValueDieB(DiceA,DiceB)
            
def changeValueDieA(A,B):
    if A[5]==4 and A[4]<4:
        A[4]=A[4]+1
        A[5]=1
        B=[1,2,3,4,5,8]
        return A,B
    else:
        A[5]=A[5]+1
        B=[1,2,3,4,5,8]
        return A,B

def changeValueDieB(DieA,DieB):
    for i in range(1,len(DieB)-1):
        DieB[i]=DieB[i]+1
    return DieA,DieB
    
def findPossComb(array1,array2,initial_sum,initial_sum_count):
    c=0
    arr=findCombination(array1,array2)
    for i in range(len(initial_sum_count)):
        res=find(arr,initial_sum_count[i],initial_sum[i])
        if res!=1:
            arr1,arr2=changeValue(array1,array2)
            findPossComb(arr1,arr2,initial_sum,initial_sum_count)
        else:
            c+=1
    if c==11:
        print(array1,array2)
        quit()
    
newDieA=[1,2,3,4,1,2]
newDieB=[1,2,3,4,5,8]

#print(findcombination(newDieA,newDieB))
# this initial_sum array consists of the possible count of all sum from 2 to 12.

initial_sum_arr=[2,3,4,5,6,7,8,9,10,11,12]
initial_sum_count_arr=[1,2,3,4,5,6,5,4,3,2,1]

findPossComb(newDieA,newDieB,initial_sum_arr,initial_sum_count_arr)