# a way to create new list from old list without a loop
#  it follows the format of [expression for value in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_upper = [fruit.upper() for fruit in fruits]
print(fruits_upper)


nums = [1, 2, -1, -5, 5, 4, 3, 2, -20]

positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]


print(positive_nums, negative_nums)

even = [num for num in nums if num % 2 == 0]
odd = [num for num in nums if num % 2 > 0]

print(even, odd)