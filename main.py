# import library random (to make random meanings)
import random

# create words bank
words_bank = ['motorway', 'petrol', 'alien',
              'plane', 'library', 'shim',
              'exams']

# create new variables
secret_word = random.choice(words_bank)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

# create and reset the variable
errors_cnt = 0

# create 'while' cycle
while True:
    letter = input('Print one English letter: ').lower()
    if len(letter) != 1:
        continue

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter

        if '*' not in gamer_word:
            print('You win :)')
            print('gassing word:', secret_word)
            break
    else:
        errors_cnt += 1
        print('Mistakes made:', errors_cnt)

        if errors_cnt == 8:
            print('You lose :(')
            print('gassing word:', secret_word)
            break

    # output gamer word
    print(''.join(gamer_word))
