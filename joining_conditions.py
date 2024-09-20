#working with Boolean operators
#user_age = int(input('what is your age, just wondering'))
#user_country = input('what is your country?')
# this is a perfect example of utilizing 'AND' 
#if user_age < 25 and user_country == 'Germany':
#    print('You can apply for a German student exchange programme')
#else:
#    print('Sorry, you do not qualify')




user_country = input('What is your country?')
# this is a perfect example of utilizing 'OR' 
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for Scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')



user_country = input('Where do you come from?')
if not user_country == 'Germany':
    print('you are not from Germany!')
else:
    print('you are from Germany')



user_age = int(input('What is your age?'))
user_country = input('What is your country')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t quality')