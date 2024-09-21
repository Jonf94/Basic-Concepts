#conceptually this first line is the start of how to set up a nested statments. I will make below a comment. 
#answer_a = input('Do you like traveling? y/n: ')
#if answer_a == 'y':
#    print('Good!')
#else:
#    print('Sorry to hear that!')


answer_a = input('Do you like traveling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia y/n: ')
    if answer_b == 'y':
        print('Excellent, you can win a ticket to Thailand!')
else:
    print('Sorry to hear that!')