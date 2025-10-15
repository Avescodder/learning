import emoji

def define_colour(_input):
    if _input == 'apple':
        print(emoji.emojize(":red_apple: is red"))
    elif _input == 'banana':
        print(emoji.emojize(":banana: is yellow"))
    elif _input == 'orange':
        print(emoji.emojize(":tangerine: is orange"))
    else:
        print("unknown")

if '__main__' == __name__:
    fruit = input("Write the fruit:\n")
    define_colour(fruit)