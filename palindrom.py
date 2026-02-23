while True:
    # Get input from the user
    input_string = input("Enter a string to check if it's a palindrome: ")
    # Remove spaces and convert to lowercase for case-insensitive comparison
    processed_string = "".join(input_string.split()).lower()
    # Reverse the string using slicing
    reversed_string = processed_string[::-1]

    # Check if the processed string is equal to its reversed version
    if processed_string == reversed_string:
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")
