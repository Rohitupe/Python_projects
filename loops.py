'''with for loop'''

number = input("enter  a name:\t")

var =""
for i in range(len(number)):
    if number[i] not in var:
        print(f"{number[i]} = {number.count(number[i])}")

        var = var + number[i]

'''with while loop'''

name = input("name:\t")
var = ""
i = 0

while i<len(name):
    if name[i] not in var:
        var = var + name[i]
        print(f"{name[i]}={name.count(name[i])}")
    i = i+1
        