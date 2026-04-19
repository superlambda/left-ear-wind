def process(num):
    # filter out non-evens
    if num % 2 != 0:
        return
    num = num * 3
    num = 'The Number: %s' % num
    return num
 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
for num in nums:
    print (process(num))
