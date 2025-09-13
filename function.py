def add(a, b):
    result = a + b
    return result
result1 = add(10, 20)
print("Addition is:", result1)

def subtract(a, b):
    result = a - b
    return result
result1 = subtract(10, 5)
print("Subtraction is:", result1)

def multiply (a, b):
    result = a * b
    return result
result1 = multiply(10, 5)
print("Multiplication is:", result1)

def divide(a, b):
    result = a / b
    return result
result1 = divide(10, 5)
print("Division is:", result1)



class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("\nAddition is:", self.a + self.b)

    def sub(self):
        print("Subtraction is:", self.a - self.b)

    def mul(self):
        print("Multiplication is:", self.a * self.b)

    def div(self):
        print("Division is:", self.a / self.b)

n1 = Calculator(20, 10)

n1.add()
n1.sub()
n1.mul()
n1.div()