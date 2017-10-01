import random

def choose_word():
    w = []
    dictionary = ['tinkoff', 'nemagia', 'hovanskiy']
    word = random.choice(dictionary)
    for i in range(len(word)):
        if word[i] not in w:
            w.append(word[i])
    return w,word

def check_letter(letter,word,w,missed,guess):
    if letter in word:
        print('Hit!')
        guess.append(letter)
    else:
        missed = missed + 1
        print('Missed, mistake ' + str(missed) + ' out of 5.')  
    string = ''        
    for i in range(len(word)):
        if word[i] in guess:
            string = string + str(word[i])
        else:
            string = string + '*'
    print('The word: ' + string)
    if missed == 5:
        print('You lost!')
    if len(guess) == len(w):
        print('You won!')
    return missed,guess    

def game(): 
    guess = []
    missed = 0
    w,word = choose_word()
    while (missed < 5) and (len(guess) < len(w)):
        print('Guess a letter:')
        letter = str(input())
        missed,guess = check_letter(letter,word,w,missed,guess)


