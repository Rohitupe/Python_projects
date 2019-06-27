# problem 1
A = 10
B = 9
X = A+B
print (f"X = {X}")


# problem 2
numbers = [10,4,32,34,543,3456,654,567,87,6789,98]
even_nums=[]
for i in numbers:
    if i%2==0:
        if i!=10:
            even_nums.append(i)
            even_nums.sort()
odd_nums=[]
for j in numbers:
    if j%2!=0:
        odd_nums.append(j)
        odd_nums.sort(reverse = True) 
total = even_nums+odd_nums
for k in total:
    print(k)


# problem 3
numbers = [7, 21, -14] 
num=numbers.sort() 
for i in numbers:
    print(i)
numbers = [7, 21, -14]
print()
for k in numbers:
    print(k)

