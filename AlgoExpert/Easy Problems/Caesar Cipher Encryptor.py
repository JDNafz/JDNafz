def caesarCipherEncryptor(string, key):
    # Write your code here.
    key = key % 26
    outString = ""
    for char in string:
        newChar = ord(char) + key
        if newChar > 122:
            newChar -= 26
        outString += (chr(newChar))
    print("outString",outString)
    return outString

    
caesarCipherEncryptor("xyz",2)