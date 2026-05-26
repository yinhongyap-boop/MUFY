def check_string(a):
    if a.startswith('The'):
        print('Found it!')
    else:
        print('Nope.')

str1='The'
str2='Thumbs up'
str3='Theatre can be boring'

print (check_string(str1))
print (check_string(str2))
print (check_string(str3))  
