class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower() 

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid operation"



a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
op = input("Enter operation (add/sub/mul/div): ")

calc = Calculator(a, b, op)
result = calc.calculate()
print("Result:", result)
