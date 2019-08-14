def main():
    name= input("Please enter a name")
    while not isValidName(name):
        print("INVALID NAME")
        name = input("Please enter a name")
    print(name[::2])

def isValidName(name):
    if len(name)< 1 :
        return False
    return True


main()


