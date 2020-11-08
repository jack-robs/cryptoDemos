import re
import string

# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters 
# @propery allows method to be called as fields - just a getter, no logic in it
# @setter, (self, arg) arg is value trying to set, put setting control logic here

# Class that holds the Caesar Cipher object
class CaesarCipher:

    # set fields you want to instantiate w/ Object here
    def __init__(self, message, key):
        self.key = key
        # hide access to this, only want access via decryption
        self.msg = message
        # TODO see how @property works with these, if I don't declare in instaniation, will @property still
        # allow these to be called directly
        self.cipherText = "run encrypt()"
        self.plainText = "run decrypt()"
    
    def encrypt(self):
        # make copy to mutate in the fxn
        workingKey = self.key
        workingMsg = self._msg.lower()
        workingCT = []

        # get copy of alphabet
        # TODO refactor into alphabetGen() or similar
        alpha = string.ascii_lowercase
        alphaList = []
        for i in range(len(alpha)):
            alphaList.append(alpha[i])
        
        #do translation, keep spaces, `a` == ascii 97, " " == 32
        for i in range(len(workingMsg)):
            unshifted = workingMsg[i]
            # skip white space
            if ord(unshifted) == 32:
                workingCT.append(unshifted)
                continue
            # actual letter
            else:
                # prob can make this math more clever, but gets to 0->25 consideration
                base = ord(unshifted) - 97
                # shift using alphaLIist
                shift = alpha[(base + workingKey) % 26]
                workingCT.append(shift)
                
    
        #TODO shift spaces logic

        self.cipherText = ''.join(workingCT)
        return self.cipherText


    '''
    getters setters
    '''
    # key getter
    @property
    def key(self):
        return self._key

    # key validation logic in here - integer nly
    @key.setter
    def key(self, value):
        try:
            value = int(value)
            self._key = value
        except ValueError:
            print("Key must be integer, i.e. 3, 5, 6,")

    # msg getter - block direct access
    @property
    def msg(self):
        block = "no access, run decrypt() and call instance.plaintext"
        return block

    # build in message validation here - no symbols etc.
    @msg.setter
    def msg(self, value):
        self._msg = value


    


