import random
numb_per_line= 6
minimum=1
maximum=45

def main():
    numb_of_picks = int(input("How many picks?: "))
    while numb_of_picks < 1:
        print("Please input a valid number.")
        numb_of_picks = int(input("How many picks?: "))

    for i in range(numb_of_picks):
        quick_pick = []
        for n in range(numb_per_line):
            number = random.randint(minimum,maximum)
            while number in quick_pick:
                number = random.randint(minimum,maximum)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))

main()