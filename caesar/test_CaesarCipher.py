# TODO move to sub-dir, fix imports 

from CaesarCipher import *

class TestCC:

    def __init__(self):
        # instantiate test class w/ expected msg and key
        self.passed_tests = []
        self.failed_tests = []
        self.total_tests = 0
    
    def testKeys(self, exp_key, act_key, testNum):
        try:
            act_key == exp_key
            testResult = "testKeys()" + str(testNum)
            self.passed_tests.append(testResult)
            self.total_tests =+ 1
            print("passed testKeys()", testNum)
        except:
            testResult = "testKeys()" + str(testNum)
            self.failed_tests.append(testResult)
            print("failed testKeys()", testNum)

    ## TODO test for ValueError for non-int key attempt

    def testMsg(self, exp_msg, act_msg, testNum):
        try:
            act_msg == exp_msg
            testResult = "testMsg()" + str(testNum)
            self.passed_tests.append(testResult)
            self.total_tests =+ 1
            print("passed testMsg()", testNum)
        except:
            testResult = "testMsg()" + str(testNum)
            self.failed_tests.append(testResult)
            print("failed testMsg()", testNum)

    ## TODO test for bad message to encrypt, w/ punctuation or numerals 

    ## TODO test init value of cipherClient.cipherText == "run encrypt()"

    # encrypt() test
    def testEncrypt(self, exp_ct, act_ct, testNum):
        try:
            act_ct == exp_ct
            testResult = "testEncrypt()" + str(testNum)
            self.passed_tests.append(testResult)
            self.total_tests =+ 1
            print("passed testEncrypt()", testNum)
        except:
            testResult = "testEncrypt()" + str(testNum)
            self.failed_tests.append(testResult)
            print("failed testEncrypt()", testNum)

    # mergeSort() and related helper fxns
    def testMSort(self, exp_sorted, act_sorted, testNum):
        
        #list compares
        sorted = True
        for i in range(len(exp_sorted)):
            if exp_sorted[i] == act_sorted[i]:
                continue
            else:
                sorted = False
                break
        
        if sorted == True:
            testResult = "testMSort()" + str(testNum)
            self.passed_tests.append(testResult)
            self.total_tests =+ 1
            print("passed testMSort()", testNum)
        else:
            testResult = "testMSort()" + str(testNum)
            self.failed_tests.append(testResult)
            print("failed testMsort()", testNum)

def main():

    # test Methods format: (exp, actual, test #)
    # basic test instance
    testClient = TestCC()

    '''
    instsance 0, CaesarCipher()
    '''

    #test safe key
    exp_msg = "a z"
    exp_key = 3
    caesarInstance = CaesarCipher(exp_msg, exp_key)
    testClient.testKeys(exp_key, caesarInstance.key, 0)

    #test no access message
    exp_msg = "no access"
    testClient.testMsg(exp_msg, caesarInstance.msg, 1)

    #test encrypt()
    exp_ct = "d c"
    caesarInstance.encrypt()
    testClient.testEncrypt(exp_ct, caesarInstance.cipherText, 2)

    '''
    instance 1, CC()
    '''
    exp_msg1 = "hello there zoo friend"
    exp_key1 = 4
    exp_ct1 = 'lipps xlivi dss jvmirh'
    caesartTest1 = CaesarCipher(exp_msg1, exp_key1)
    caesartTest1.encrypt()
    testClient.testEncrypt(exp_ct1, caesartTest1.cipherText, 3)

    # test mergesort, using exp_ct1
    exp_sorted1 = ['d', 'h', 'i', 'i', 'i', 'i', 'j', 'l', 'l', 'm', 'p', 'p', 'r', 's', 's', 'v', 'v', 'x']
    testClient.testEncrypt(exp_sorted1, caesartTest1.mergeSort(exp_ct1), 4)

    print("Failed", len(testClient.failed_tests))
    print("Passed", len(testClient.passed_tests))



main()







