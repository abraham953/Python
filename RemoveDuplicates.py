list=[0,2,2,4]
uniques=[]
for number in list:
    if number not in uniques:
        print(number)
        uniques.append(number)
print(uniques)


