from random import randint


def gen_num(num):
    """
    Generate a string of "num" that will appear random times.

    :param num: a number.

    :return: string of the number X times.
    """
    string = ""
    for _ in range(randint(1, 20)):
        string += str(num)
    return string


def check_input():
    """

    :return: check if the input is valid and return the valid input, as an int
    """
    jump = input("please enter how many jumps you want to take? ")
    if jump.isdigit():
        jump = int(jump)
        if 1 <= jump <= 408:
            return jump

        else:
            print("please enter a number between 1 - 408")
            return check_input()

    else:
        print("wrong input.\nplease enter a number.")
        return check_input()


def check_direction():
    """
    check if the input is valid
    :return: True if user want to move forward, False if user wants to move backwards.
    """
    direct = input("for moving forward press f for moving backward press b ").lower()
    if direct == "f":
        return True
    elif direct == "b":
        return False
    else:
        print("Please enter a valid input")
        return check_direction()


def check_win(char):
    if char.isdigit():
        return True
    print("You have won!")
    return False


# Creating a new file
with open("Treasure_Island.txt", mode="w") as file:
    for number in range(10):
        file.write(gen_num(number))

    file.write("TREASURE")

    for number in range(9, -1, -1):
        file.write(gen_num(number))

print("Welcome to the Treasure Island game")
game_is_on = True

# Open the file for the game
with open("Treasure_Island.txt") as file:
    record = file.readline()
    file.seek(0)
    while game_is_on:
        if check_direction():
            steps = check_input()
            file.seek(file.tell() + steps)
            if record[file.tell():file.tell() + 1] == "":
                print("You've passed the end of the file. You've been moved back to the last char ")
                file.seek(len(record) - 1)
            print(file.tell())
            print(record[file.tell():file.tell() + 1])
            game_is_on = check_win(record[file.tell():file.tell() + 1])

        else:
            steps = check_input()
            try:
                file.seek(file.tell() - steps)
            except ValueError:
                print("You are at the beginning. You cannot move forward")
            else:
                print(file.tell())
                print(record[file.tell():file.tell() + 1])
                game_is_on = check_win(record[file.tell():file.tell() + 1])
