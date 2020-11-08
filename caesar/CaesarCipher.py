import re

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
        block = "no access"
        return block

    # build in message validation here - no symbols etc.
    @msg.setter
    def msg(self, value):
        self._msg = value

    


