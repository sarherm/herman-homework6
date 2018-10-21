import re
import unittest

def sumNums(fileName):
    openFile = open(fileName, 'r')
    lines = openFile.read()
    
    integers = re.findall(r'[0-9]+', lines)

    total = 0 
    for x in integers:
        total += int(x)
    openFile.close()
    return total  

def countWord(fileName, word):
    openFile = open(fileName, 'r')
    data = openFile.read()
    
    words = re.findall(r"(?i)" + str(word) + "(?!\w+)", data)
    
    return len(words)


    #pass

def listURLs(fileName):
    openFile = open(fileName, 'r')
    data = openFile.read()
    urls = re.findall(r"\S+\.\S+\.\w+", data)

    return urls


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
