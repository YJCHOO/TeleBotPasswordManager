#import random
import random


#Password length = 8 contains 
# - Upper case 
# - Lower case
# - Numberical 
# - Punctuation

class PasswordGenerator:
    #Max password length
    length = 8

    #ascii code for lower case a-z
    lower_case_ascii = [97, 122] 

    #ascii code for upper case A-Z
    upper_case_ascii = [65, 90]

    #ascii code for number 0-9
    numberical_ascii = [48, 57]

    #ascii code for punctuation mark, call displayPunctuationASCII() to see content inside.
    punctuation_ascii = [[33, 47], [58,64], [91, 96], [123, 126]] 

    function_list = []

    def __init__(self):
        self.function_list.extend([self.lowerCaseGenerator, self.upperCaseGenerator, self.numbericalGenerator, self.punctuationGenerator])


    def generatePassword(self):
        password = ""
        passwordList = random.sample(self.function_list, 4) #pick 4 mandatory generator
        passwordList.extend(random.choices(self.function_list, k=4)) #random pick from 4 generator
        random.shuffle(passwordList) #shuffle the sequence
        for i in passwordList: 
            password+= chr(i())
        return password

    def lowerCaseGenerator(self):
        return random.randint(self.lower_case_ascii[0], self.lower_case_ascii[1])

    def upperCaseGenerator(self):
        return random.randint(self.upper_case_ascii[0], self.upper_case_ascii[1])

    def numbericalGenerator(self):
        return random.randint(self.numberical_ascii[0], self.numberical_ascii[1])

    def punctuationGenerator(self):
        picker = random.randint(0, len(self.punctuation_ascii) - 1)
        return random.randint(self.punctuation_ascii[picker][0], self.punctuation_ascii[picker][1])

    def displayPunctuationASCII(self): 
        for i in self.punctuation_ascii:
            for index in range(i[0], i[1] + 1):
                print( 'Decimal ' + str(index) + ' = ' + chr(index))
