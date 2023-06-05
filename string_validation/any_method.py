if __name__ == '__main__':
    s = input()

# Check for alphanumeric characters
print(any(c.isalnum() for c in s))

# Check for alphabetical characters
print(any(c.isalpha() for c in s))

# Check for digits
print(any(c.isdigit() for c in s))

# Check for lowercase characters
print(any(c.islower() for c in s))

# Check for uppercase charcters
print(any(c.isupper() for c in s))
