class Question:
    answer = None 
    text = None

class Add(Question):
    def __init__(self, num1, num2):
        self.text = f'{num1} + {num2}'
        self.answer = num1 + num2

class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = f'{num1} X {num2}'
        self.answer = num1 * num2

class Divide(Question):
    def __init__(self, num1, num2):
        self.text = f'{num1} / {num2}'
        self.answer = num1 / num2

class Substract(Question):
    def __init__(self, num1, num2):
        self.text = f'{num1} - {num2}'
        self.answer = num1 - num2