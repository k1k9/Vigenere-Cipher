from string import ascii_uppercase

''' DECRYPT GIVEN TEXT WITH KEY (VIGENERE METHOD) '''
def decrypt(key, encrypted, table):

    # SEARCH ELEMENTS
    _ki = -1 # Key Iterrator
    key_text = ''

    for i in range(len(encrypted)):
        # loop over key
        _ki = 0 if (_ki == len(key)-1) else (_ki + 1)

        if not encrypted[i].isalpha():
            key_text += encrypted[i]
            _ki -= 1
            pass

        column = ascii_uppercase.index(key[_ki].upper())

        # Find encrypted char in caesar table
        for j in range(len(ascii_uppercase)):
            if table[j][column] == encrypted[i].upper():
                key_text += table[j][0] if encrypted[i].isupper() else table[j][0].lower()
                
    print(key_text)
