def loop_list():
    print("\n----For Loop List  Break conditionExample----")
    fruits = ["apple", "banana", "cherry", "mango"]
    for fruit in fruits:
        if fruit == "cherry":
            break
        print(fruit)
loop_list()

def loop_list():
    print("\n----For Loop list Continous Condition Example----")
    fruits = ["apple", "banana", "cherry", "mango"]
    for  fruit in fruits:
        if fruit == "banana":
            continue
        print(fruit)
loop_list()

def loop_set():
    print("\n----For Loop Set Continous Condition Example----")
    numbers = {1, 2, 3, 4, 5, 6, 3, 2, 0, 3, 1}
    for number in numbers:
        if number == 3:
            continue
        print(number)
loop_set()

def loop_set():
    print("\n----For Loop Set Break Condition Example----")
    numbers = {1, 2, 3, 4, 5, 6, 3, 2, 0, 3, 1}
    for number in numbers:
        if number == 3:
            break
        print(number)
loop_set()


def loop_dic():
    print("\nLoop Dictionary Example:")
    student = {"Name": "Alice", "Age": 20, "Grade": "A"}
    for key in student:
        if key == "Age":
            continue
        print(f"{key} -> {student[key]}")
loop_dic()

def loop_dic():
    print("\n----For Loop Dictionary Break Condition example----")
    student = {"Name": "Alice", "Age": 20, "Grade": "A"}
    for key in student:
        if key == "Age":
            break
        print(f"{key} -> {student[key]}")
loop_dic()