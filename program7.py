#Output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values using List Comprehension


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


odd_cubes = {n: n**3 for n in numbers if n % 2 != 0}

# Output dictionary
print(odd_cubes)
