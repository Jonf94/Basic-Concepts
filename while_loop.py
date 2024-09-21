counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')
#also avoid creating an infinite loop- make sure to always include your counter

secret_number = 14
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret_number from from o 20'))
print('Perfect! you have guessed the secret number ')