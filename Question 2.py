str = input("Enter a string: ")
rev_str = str[ :: -1]
if str.lower() == rev_str.lower():
    print("String is palindrome")
else:
    print("String is not palindrome")