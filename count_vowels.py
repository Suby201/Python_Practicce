vowels = "aeiou"
count = 0
str = 'Python is awesome'
for char in str:
    if char in vowels:
        count += 1
print(f'모음 개수 : {count}')