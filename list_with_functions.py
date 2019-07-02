# exercise 1
stri = ['abc','tuv','xyz']

def reverse(stri):
    st = []
    for i in stri:
        st.append(i[::-1])
    print(st)
reverse(stri)




# exercise 2
list1 = [1,2,3,4,5,6,7,8,9]

def odd_even(list1):
    even = []
    odd = []
    for i in list1:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
print(odd_even(list1))


# exercise 3  take union
l1 = [1,2,3,4]
l2 = [1,2,5,6]

def check(l1,l2):
    empty = []
    for i in l1:
        if i in l2:
            empty.append(i)
    return empty
print(check(l1,l2))

# exercise 4
list3 = [1,2,66,43,565,78,845,4,532]

print(max(list3))
print(min(list3))


# exercise 5
list5 = [1,2,3,[1,2,3,4,5],[12,3,3,5,]]

def count(list5):
    list9 = []
    count = 0
    for i in list5:
        if type(i) == list:
            list9.append(i)
            count = count + 1 
        # print(i)
    print(count)
    print(list9)  
count(list5)






