# write text data in file
with open('./assets/data.txt', 'w') as file:
    file.write('Marwadi University')
    
# append text data in file
with open('./assets/data.txt', 'a') as file:
    file.write('\nComputer Application')

# read text data in file
with open('./assets/data.txt') as file:
    print(file.read())

# read and create duplicate file for binary data in file
with open('./assets/logo.png', 'rb') as file:
    binary = file.read()
    
with open('./assets/logo_copy.jpg', 'wb') as file:
    file.write(binary)

lst = ['Hello\n', 'World!\n', 'Marwadi\n', 'University']
# writelines data in file
with open('./assets/data.docx', 'w') as file:
    file.writelines(lst)

#reading the above
with open('./assets/data.docx') as file:
    print('As Readlines: ', file.readlines())
    print('As readline:- ')
    
    file.seek(0)
    #reads five characters
    print(file.readline(5), end='')