#need to solve all the 26 patterns in the dsa
#to get a job 

n = [9,6,4,2,3,5,7,0,1]
ans = 9
for i in range(1, len(n)):
    ans ^= n[i]
print(ans)
