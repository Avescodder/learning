def ask():
    answer_inp = ["yes", "no"]
    weather = input("Is it raining?:\n").lower()
    windy = input("Is it windy?\n").lower()
    if weather in answer_inp and windy in answer_inp:
        return answer(weather, windy)
    else:
        print("Please answer only 'yes' or 'no'.")
        return ask()


def answer(weather, windy):
        if weather == "yes" and windy == "yes":
            print("It is too windy for an umbrella")

        elif weather == "yes":
            print("Take an umbrella")

        else:
            print("Enjoy your day")


if __name__ == '__main__':
    ask()
