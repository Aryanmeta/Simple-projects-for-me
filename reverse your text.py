text = input('Type your text: ')
for word in text.split():
    print(word[::-1], end=" ")