def count_words(sentence):
    words = sentence.split()
    return len(words)

num = count_words("Hello, how are you?")
print(f'단어 수 : {num}')
