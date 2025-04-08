dict1 = {"name" : "John", "age" : 30}
dict2 = {"math" : 90, "science" : 85, "history" : 78}
dict3 = {"apple" : 3, "bananana" : 5}
print(f'나이: {dict1["age"]}')
subject = dict2.keys()
print(f'과목들: {subject}')
dict3["apple"] += 2
print(dict3)