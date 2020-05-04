
''' DECRYPT GIVEN TEXT WITH KEY (VIGENERE METHOD) '''
def decrypt(key, encrypt):
    
    ##############################
    # CREATE CAESAR TABLE
    ##############################
    from string import ascii_uppercase
    table = []

    for i in range(len(ascii_uppercase)):
        table.append([]) # Create row

        for j in range(i, len(ascii_uppercase)):
            table[i].append(ascii_uppercase[j])
        
        for j in range(0, i):
            table[i].append(ascii_uppercase[j])




    ##############################
    # SEARCH ELEMENTS
    ##############################
    _ki = -1 # Key Iterrator
    key_text = ''

    for i in range(len(encrypt)):
        # loop over key
        _ki = 0 if (_ki == len(key)-1) else (_ki + 1)

        if not encrypt[i].isalpha():
            key_text += encrypt[i]
            _ki -= 1
            pass

        column = ascii_uppercase.index(key[_ki].upper())

        # Find encrypted char in caesar table
        for j in range(len(ascii_uppercase)):
            if table[j][column] == encrypt[i].upper():
                key_text += table[j][0] if encrypt[i].isupper() else table[j][0].lower()




    print(key_text)