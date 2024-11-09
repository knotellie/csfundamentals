print('Enter a word and I will reverse it!')
word = input() 

def word_reverser(word): #Word is the argument and also the parameter
    return word[::-1]

result = word_reverser(word) #Calling the function

print(result)