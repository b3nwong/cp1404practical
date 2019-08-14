def main():
    name = get_name()
    while not isValidName(name):
        print("INVALID NAME")
        name = get_name()
    print_name_frequency(name,3)


def print_name_frequency(name,n):
    print(name[::n])


def get_name():
    name = input("Please enter a name: ")
    return name


def isValidName(name):
    if len(name)< 1 :
        return False
    return True


main()


