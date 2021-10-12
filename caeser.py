# Caesar cipher.
text = input("Enter your message: ")
shift=int(input("enter the shift value:"))
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + shift
    if shift + ord(char)> ord('Z'):
        code = ord('A')+(shift-(ord('Z')-ord(char)+1))
    cipher += chr(code)

print(cipher)
