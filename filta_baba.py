alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
vowels = ['a', 'e', 'i', 'o', 'u']
output = list(filter(lambda x: (x in vowels) , alphabets))
# Output: ['a', 'e', 'i']
print(output)

