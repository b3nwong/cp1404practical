colour_codes = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0",
                "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4",
                "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74",
                "azure1": "#f0ffff"}

user_colour = input("what colour do you want the code for?: ")
while user_colour != "":
    if user_colour in colour_codes:
        print("Your code is {}.".format(colour_codes[user_colour]))
        user_colour = input("what colour do you want the code for?: ")
    else:
        print("Invalid colour!")
        user_colour = input("what colour do you want the code for?: ")

