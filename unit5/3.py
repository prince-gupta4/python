class Vote(Exception):
    pass

try:
    age = int(input('Enter age: '))
    if(age>17):
        print('You can vote')
    else:
        raise Vote('You cannot Vote.')
except Exception as e:
    print('Error: ', e)