import os
import sys

path = os.getcwd()
print(path)

folder = os.path.join(path, "Storage")
filename = os.path.join(folder, "data.txt")
sorryfile = os.path.join(folder, "sorry_file.txt")

print(os.path.isdir(r"d:/prince"))
print(os.path.isfile(r"d:/prince/unit3/1.py"))
print(os.path.isabs(filename))

if not os.path.exists(folder):
    print("Storage Directory created.")
    os.makedirs(folder)

with open(filename, 'w') as file:
    file.write("Hello world!")
    file.writelines(" Welcome")
    file.writelines("\nMarwadi University")

with open(sorryfile, 'w') as file:
    for i in range(1, 2000):
        file.writelines("I'm really Sorry!\n")
    file.close()

#read using with
print()
with open(filename, 'rt') as file:
    print(file.read())
    file.close()

#read using without with
print()
def reading():
    fs = open(filename)
    print(fs.read())
    fs.close
reading()


#append
with open(filename, 'a') as file:
    file.write("\nPython Lab")
    print()
    file.close()
    reading()

#Sys Library
if len(sys.argv) > 1:
    i = 0
    for arg in sys.argv:
        print(f"Sys argurement {i}: ", arg)
        i += 1
else:
    print('\nSys arguement 0(Script name): ',sys.argv[0])


if os.path.exists('helper'):
    os.removedirs('helper')
    print("Helper Folder Deleted")
else:
    print("Helper Folder doesn't exist")
    
if os.path.exists('helper.txt'):
    os.remove('helper.txt')
    print("Helper File Deleted")
else:
    print("Helper File doesn't exist")

print("\nCPU count: ", os.cpu_count())
print("\nSys Platform: ", sys.platform)
print("\nSys Version: ", sys.version)

sys.exit(0)
