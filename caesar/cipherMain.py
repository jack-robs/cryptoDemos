from CaesarCipher import *

def main():
    '''
    Caesar cipher
    Has tests
    encodes with monoalphabetic numeric shift 
    '''
    
    # set message & key: no symbols for now TODO support punctuation 
    message = "a z"
    key = 3

    # instantiate CaesarCipher(), 
    # direct call to session.msg will fail on purpose (only want session.plaintext) to work, which only works after runing decrypt()
    session = CaesarCipher(message, key)
    session.encrypt()

    #print(session.key)
    #print(session.msg)
    #print(session._msg)
    # encrypt 

    # get ciphertext 

    # decrypt 

    # get plaintext




main()
