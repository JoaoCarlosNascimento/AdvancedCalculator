import numpy as np
import matplotlib.pyplot as plt
import os.path
from os import path
from mpl_toolkits import mplot3d


def insert_file_name(number):
    if number == "1":
        file_name = input("Insert the name for your Note file: ") + ".txt"
        while path.exists(file_name):
            print("Invalid, insert a new name for your Note file!")
            file_name = input("Insert a valid name for your Note file: ") + ".txt"
        return file_name
    else:
        file_name = input("Insert the name of your Note file: ") + ".txt"
        while not path.exists(file_name):
            print("Invalid, insert an existing name of your Note file!")
            file_name = input("Insert a valid name for your Note file: ") + ".txt"
        return file_name


print("Welcome to the Advanced Calculator,here are the features:")
option = int(input("1 - Arithmetic Operations\n2 - Algebraic Operation\n3 - Notes\n4 - Graphs\n5 - Matrix Operations\n"))
while option < 1 or option > 5:
    option = int(input("Insert a valid option: "))


if option == 1:  # Arithmetic Operations
    print("-----------------------------------------------------------------------------")
    option2 = int(input("1 - Addition(+)\n2 - Subtraction(-)\n3 - Multiplication(*)\n4 - Division(/)\n"))
    while option2 < 1 or option2 > 4:
        option2 = int(input("Insert a valid option: "))

    if option2 == 1:
        try:
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))

        except ValueError:
            print("Insert valid numbers!!")
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))
        result = num1 + num2
        print("Result: " + str(result))

    if option2 == 2:
        try:
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))

        except ValueError:
            print("Insert valid numbers!!")
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))
        result = num1 - num2
        print("Result: " + str(result))

    if option2 == 3:
        try:
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))

        except ValueError:
            print("Insert valid numbers!!")
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))
        result = num1 * num2
        print("Result: " + str(result))

    if option2 == 4:
        try:
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))

        except ValueError:
            print("Insert valid numbers!!")
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))
        result = num1 / num2
        print("Result: " + str(result))


if option == 2:  # Algebraic Operation
    print("-----------------------------------------------------------------------------")
    print("Formula used: (-b\u00B1\u221A((b**2)-4ac))/2a")
    print("Insert the numbers from the highest degree to the lowest: ")
    try:
        num1 = float(input("Insert a: "))
        num2 = float(input("Insert b: "))
        num3 = float(input("Insert c: "))

    except ValueError:
        print("Insert valid numbers!!")
        num1 = float(input("Insert a: "))
        num2 = float(input("Insert b: "))
        num3 = float(input("Insert c: "))

    first = ((num2 ** 2) - (4 * num1 * num3)) ** (1 / 2)
    Result1 = (-first - num2) / (2 * num1)
    Result2 = (first - num2) / (2 * num1)
    print("First Result: " + str(Result1) + "\nSecond Result: " + str(Result2))

if option == 3:  # Notes
    print("-----------------------------------------------------------------------------")
    print("1 - Create new Note\n2 - View existing Note\n3 - Add to existing Note")
    option3 = int(input("4 - Delete Note\n5 - OverWrite an existing Note\n"))
    while option3 < 1 or option3 > 5:
        option3 = int(input("Insert a valid option: "))

    if option3 == 1:
        name = insert_file_name("1")
        file = open(name, "w")
        content = input("Insert the content for your new Note: ")
        file.write(content)
        file.close()

    if option3 == 2:
        name = insert_file_name("2")
        file = open(name, "r")
        if file.readable():
            print(file.read())
            file.close()
        else:
            print("The file is not readable")

    if option3 == 3:
        name = insert_file_name("3")
        file = open(name, "a")
        add_content = "\n" + input("Insert new content to add to your Note: ")
        file.write(add_content)
        file.close()

    if option3 == 4:
        name = insert_file_name("4")
        os.remove(name)

        if not path.exists(name):
            name = name.replace('.txt', '')
            print(name + " has been deleted!")

    if option3 == 5:
        name = insert_file_name("5")
        file = open(name, "w")
        add_content = "\n" + input("Insert new content to add to your Note: ")
        file.write(add_content)
        file.close()

if option == 4:  # Graphs
    option4 = input("1 - Graph in 2 dimensions\n2 - Graph in 3 dimensions\n")
    while option2 < 1 or option2 > 2:
        option2 = int(input("Insert a valid option: "))

    if option4 == 1:
        option41 = int(input("1 - Create graph using the equation: y=ax+b\n2 - Create graph by putting each point\n"))
        if option41 == 1:
            try:
                a = float(input("Insert a: "))
                b = float(input("Insert b: "))

            except ValueError:
                print("Insert valid numbers!!")
                a = float(input("Insert a: "))
                b = float(input("Insert b: "))

            index = 0
            y_value = []
            x_value = []
            for index in range(0, 10):
                y_value.append(a * index + b)
                x_value.append(index)

            plt.plot(x_value, y_value)
            plt.show()
        if option41 == 2:
            number = int(input("How many points do you want: "))
            y_value = []
            x_value = []
            for index in range(number):
                point_x = float(input("X coordinate for the point[" + str(index) + "]: "))
                point_y = float(input("Y coordinate for the point[" + str(index) + "]: "))
                y_value.append(point_y)
                x_value.append(point_x)

            plt.plot(x_value, y_value)
            plt.show()

    if option4 == 2:
        ax = plt.axes(projection="3d")
        number_points = int(input("Insert the number of points to draw each label: "))
        Lower_Limit = [0, 0, 0]
        Upper_Limit = [100, 100, 100]

        x = np.linspace(Lower_Limit[0], Upper_Limit[0], 100)
        y = np.linspace(Lower_Limit[1], Upper_Limit[1], 100)
        z = np.linspace(Lower_Limit[2], Upper_Limit[2], 100)

        Lower_Limit.append(int(input("Lower Limit to X: ")))
        Upper_Limit.append(int(input("Upper Limit to X: ")))
        Lower_Limit.append(int(input("Lower Limit to Y: ")))
        Upper_Limit.append(int(input("Upper Limit to Y: ")))
        Lower_Limit.append(int(input("Lower Limit to Z: ")))
        Upper_Limit.append(int(input("Upper Limit to Z: ")))

        ax.plot3D(x, y, z)
        plt.show()

