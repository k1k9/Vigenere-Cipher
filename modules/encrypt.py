from string import ascii_uppercase

''' ENCRYPT GIVEN TEXT WITH KEY (VIGENERE CIPHER) '''
def encrypt(key,text,table):

    # CHANGE TEXT TO KEY TEXT
    key_text = ''
    x = -1

    for i in range(len(text)):
        # key length control
        x = 0 if (x == len(key)-1) else (x + 1)

        # Check is char must be in upper or lowercase
        _key_char = key[x].upper() if text[i].isupper() else key[x].lower()

        # Check special characters
        if text[i].isalpha():
            key_text += _key_char
        else:
            key_text += text[i]
            x -= 1


    # ENCRYPTION THE KEY_TEXT
    encrypted = ''

    for i in range(len(text)):
        # Locate letter in caesar table
        column = ascii_uppercase.index(text[i].upper()) if text[i].isalpha() else False
        row    = ascii_uppercase.index(key_text[i].upper()) if key_text[i].isalpha() else False

        if column or row:
            encrypted += table[row][column] if key_text[i].isupper() else table[row][column].lower()
        else:
            encrypted += text[i]


    print(encrypted)
    