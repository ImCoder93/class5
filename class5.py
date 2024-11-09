fruit=['orange','mango','kiwi']
print(fruit)
print(fruit[0])#positive index
print(fruit[-2])#negative index
print(fruit[0:2])#slicing
print(fruit[0:1])
fruit.append('apple')#adding values
fruit.append('strawberry')
fruit.remove('orange')#removing orange
fruit.pop(2)
if'apple'in fruit:
    print('yes')
else:
    print('no')
if'strawberry'in fruit:
    print('yes')
else:
    print('no')
for i in fruit:
    print(i)

