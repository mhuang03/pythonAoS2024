string = input("type something: ")

for i in range(len(string)//2):
    if string[i] != string[-(i+1)]:
        print("Not a palindrome!")
        break
else:
    print("Palindrome!")


# print("Palindrome!" if string == string[::-1] else "Not a palindrome!")