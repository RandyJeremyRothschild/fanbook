num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

count = 0

for num in num_list:
    if num % 2 == 0:
        count += 1

print(count)