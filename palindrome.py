def is_palindrome(text):
    """
    Checks if a given string is a palindrome.

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove spaces for case-insensitive
    # and space-agnostic comparison.
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())

    # Compare the cleaned string with its reverse.
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome("madam"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))
print(is_palindrome("Racecar"))