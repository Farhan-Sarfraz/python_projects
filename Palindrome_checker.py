def is_palindrome_stack(text):
    stack = []
    for char in text:
        if char.isalnum():
            stack.append(char.lower())
    reversed_text = ''
    while stack:
        reversed_text += stack.pop()
    cleaned_text = ''.join([c.lower() for c in text if c.isalnum()])
    return cleaned_text == reversed_text

def is_palindrome_recursive(text):
    cleaned = ''.join([c.lower() for c in text if c.isalnum()])
    def helper(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return helper(s[1:-1])
    return helper(cleaned)

def palindrome_checker():
    print("Palindrome Checker ")
    user_input = input("Enter a word or sentence: ")
    stack_result = is_palindrome_stack(user_input)
    recursive_result = is_palindrome_recursive(user_input)
    print(f"\nUsing Stack: {'Palindrome' if stack_result else 'Not a Palindrome'}")
    print(f"Using Recursion: {'Palindrome' if recursive_result else 'Not a Palindrome'}")

if __name__ == "__main__":
    palindrome_checker()
