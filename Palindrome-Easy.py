while True:
    word = input("Enter a Word to check Palindrome : ")

    rev = word[::-1]

    if rev == word:
        print("Yes, It is a Palindrome")

    else:
        print("No, It is not a Palindrome")