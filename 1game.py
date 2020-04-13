import random

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1,20)
print('Хорошо, {}, я загадал число от 1 до 20. У тебя 6 попыток, чтобы отгадать число.'.format(myName))

for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    guessesTaken =str(guessesTaken + 1)
    print('Отлично, {}! Ты справился за {} попыток!'.format(myName, guessesTaken))

if guess != number:
    number=str(number)
    print('Увы, ты проиграл. Я загадал число {}.'.format(number))