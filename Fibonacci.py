# def fibo_list(max):
#     nums = []
#     a , b = 0 , 1
#     while len(nums) <= max:
#         nums.append(b)
#         a , b = b, a + b
#     return nums


# Generator

def fibo_generator(max):
    x = 0 
    y = 1
    count = 0

    while count < max:
        x, y = y, x + y
        yield y
        count += 1

for num in fibo_generator(8):
    print(num)
