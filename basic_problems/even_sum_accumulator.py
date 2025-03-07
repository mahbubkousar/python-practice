def even_sum_accumulator(nums):
    even_sum = 0

    for num in nums:
        if(num % 2 == 0):
            even_sum += num
    
    return even_sum

test_input = [1, 2, 3, 4, 5, 6]

result = even_sum_accumulator(test_input)
print(result)

