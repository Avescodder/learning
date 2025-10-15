
def greet(surname, name, age):
    print("Hello, welcome to the program!")
    name = input("What is your name?\nEnter name: ")
    surname = input("What is your surname?\nEnter surname: ")
    age = input("What is your age?\nEnter age: ")
    return surname, name, age

def main():
    surname = ""
    name = ""
    age = 0
    surname, name, age = greet(surname, name, age)
    print(f"Hello, my name is {name} {surname} and I am {str(age)} years old.")

if __name__ == "__main__":
    main()