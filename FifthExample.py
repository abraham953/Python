name = input('What is your name?')
length = len(name)
print(length)
if length < 3:
    print('The name is too short')
elif length > 50:
    print('The name is too ling')
else:
    print('The name looks good!!!')