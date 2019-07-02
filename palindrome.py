def palin(string):
    if string == string[::-1]:
        print(string)
        print("True")
    else:
        print("This string is not plaindrome")
        print("false") 
palin("madam")