import sys
data = sys.stdin.read().splitlines()

r = 0
flag = 0
if data[0][0] != "F" and data[0][0] != "B" :
    r = int(data[0]) + 3
elif data[1][0] != "F" and data[1][0] != "B" :
    r = int(data[1]) + 2
elif data[2][0] != "F" and data[2][0] != "B" :
    r = int(data[2]) + 1
if r % 3 == 0 and r % 5 == 0 :
    print("FizzBuzz")
elif r % 3 == 0 :
    print("Fizz")
elif r % 5 == 0 :
    print("Buzz")
else :
    print(r)