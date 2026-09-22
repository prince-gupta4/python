import re
import os

folder = os.getcwd()
filename = os.path.join(folder, 'Storage/data.txt')

with open(filename, 'r') as file:
    file_content = file.read()

university = re.search(r'[mM][\w]+\s[\w]+y', file_content)
print('University name from file: ', university.group())