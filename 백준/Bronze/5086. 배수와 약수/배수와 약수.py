def case_finder(nums) :
    a = nums[0] // nums[1]
    b = nums[0] / nums[1]
    c = nums[1] // nums[0]
    d = nums[1] / nums[0]
    if a == b :
        return 'multiple'
    elif c == d :
        return 'factor'
    else :
        return 'neither'
    
while True :
    data = list(map(int, input().split()))
    if data[0] == 0 and data[1] == 0 :
        break
    r = case_finder(data)
    print(r)