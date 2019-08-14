import os

print("The files in this folder are {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)