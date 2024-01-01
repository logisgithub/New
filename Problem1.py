#total dices = 2 (six-sided)
N=2
dice_combination=[(i,) for i in range(1,7)]

for i in range(1,N):
    newcomb=[]
    for j in dice_combination:
        for k in range(1,7):
            newcomb.append(j+(k,))
    dice_combination=newcomb


#1) Total number of combinations
total_combination=1
i=1
while i<=N:
    total_combination=total_combination*6
    i+=1
print(total_combination)


#2) Total combinations

print(dice_combination)


#3)Probability of all possible sums

def psum(arr,x):
    count=0
    for i in range(len(arr)):
        s=0
        for j in range(len(arr[i])):
            s+=arr[i][j]
        if s==x:
            count+=1
    return count

for i in range(2,(N*6)+1):
    p_sum=1/psum(dice_combination,i)
    print("The probability of all possible sum for %d is %.2f"%(i,p_sum))
