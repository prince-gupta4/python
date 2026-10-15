with open('./assets/data.docx') as file:    
    print('Pointer is at:- ', file.tell())
    print('\nPutting pointer at 7 and read 1 line.')
    file.seek(7)
    print(file.readline(), end='')
    print('Now, Pointer is at:- ', file.tell())