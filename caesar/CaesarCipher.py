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

    def decrypt(self):
        '''
        frequency analysis
        idea:
            - to do frequency anaylsis, need to count occurnce of each
            letter in the cipher text
            - it's probably easier to count if it's sorted prior to
            counting each individual letter in the cipher
            - so, cipherText -> cipherTextList -> sort cipherTextList
            - count CipherTextListSorted occurnece of each letter
            - go from there
        '''


    def mergeSort(self, cipherText):
        '''
        merge sort helper function
        cipherText str
        '''

        # split cipher string into list of individual chars
        cipherList = list(cipherText)

        # list to sort, lo ,hi
        self.sort(cipherList, 0, len(cipherList)-1,)

        # sorted, use for frequeny analysis in decrypt
        return cipherList

    def sort(self, toSort, lo, hi):
        '''
        merge sort helper
        '''
        if hi <= lo:
            return

        # se new mid
        mid = lo + (hi - lo) / 2
        self.sort(toSort, lo, mid)
        self.sort(toSort, mid + 1, hi)
        self.merge(toSort, lo, mid, hi)

    def merge(self, toSort, lo, mid, hi):

        # make aux array
        aux = []
        
        # set index trackers
        i = lo
        j = mid + 1

        #copy into aux array
        k = lo
        while k <= hi:
            aux[k] = toSort[k]
            k += 1
        
        # merge back into toSort
        k = lo
        while k <= hi:
            if i > mid: 
                toSort[k] = aux[j]
                j += 1
            elif j > hi:
                toSort[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]: 
                toSort[k] = aux[j]
                j += 1
            else:
                toSort[k] = aux[i]
                i += 1

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


    


