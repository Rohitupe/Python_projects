
def num(l):
    pop_num = []
    for i in range(1,len(l) + 1):
        poped = l.pop()
        pop_num.append(poped)
    return pop_num 

number = [1,2,3,4]
# for i in range(1,len(number) + 1):
#     print(i)
print(num([1,2,3,4]))
