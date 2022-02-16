#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def checkGuess(guess, answer):
    mock = answer
    pos = 0
    output = ['-','-','-','-','-']
    while pos < 5:
        if guess[pos] == answer[pos]:
            output[pos] = 'G'
            mock = mock[0:mock.index(guess[pos])] + mock[mock.index(guess[pos])+1:len(mock)]
        pos += 1
    pos = 0
    while pos < 5:
        if guess[pos] in mock and output[pos] != 'G':
            output[pos] = 'Y'
            mock = mock[0:mock.index(guess[pos])] + mock[mock.index(guess[pos])+1:len(mock)]
        pos +=1
    result = ''
    for c in output:
        result += c
    return result
            

word_list = []
file = open("words.txt")
for word in file:
    word_list.append(word.strip().lower())

ans = random.choice(word_list)

guesses = 0

while guesses < 6:
    guess = input("Enter a 5 character word: ")
    #if guess not in word_list:
    #    print("not a valid word!")
    #    continue
    if len(guess) != 5:
        print("not a valid word!")
        continue
    output = checkGuess(guess, ans)
    print(output)
    if(output == 'GGGGG'):
        print('-----------------')
        print("Congrats you won!")
        quit()
    
    guesses += 1

print('-----------------')
print("You Lost! The word was", ans)