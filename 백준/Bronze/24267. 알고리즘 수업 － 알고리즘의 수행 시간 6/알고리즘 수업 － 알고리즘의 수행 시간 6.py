n = int(input())
count = 0
temp = [0,0,1,4]
if n < 5 :
    count = temp[n-1]
else :
    for k in range(1, n-1) :
        count += (k)*(k+1)//2
print(int(count))
print('3')