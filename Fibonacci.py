def fibo_list(max):
    nums = []
    a , b = 0 , 1
    while len(nums) <= max:
        nums.append(b)
        a , b = b, a + b
    return nums
