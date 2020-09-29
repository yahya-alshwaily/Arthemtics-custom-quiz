import datetime
import random

from mathquiz1 import Add, Multiply, Divide, Substract

class Quiz:

    questions = []
    answers = []
    answer_times = []
    times = [10000]
    shortest_time = min(times)
    def __init__ (self, operations, num_questions, num_range_low, num_range_high):

        question_types = []
        if '1' in operations:
            question_types.append(Add)
        if '2' in operations:
            question_types.append(Substract)
        if '3' in operations:
            question_types.append(Multiply)
        if '4' in operations:
            question_types.append(Divide)
        while len(self.questions) < num_questions:

            num1 = random.randint(num_range_low, num_range_high)
            num2 = random.randint(num_range_low, num_range_high)
            try:
                question = random.choice(question_types)(num1, num2)
            except ZeroDivisionError:
                continue
            self.questions.append(question)

    def take_quiz(self):

        self.start_time = datetime.datetime.now()
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
            
        return self.summary()


    def ask(self, question):
        correct = False 
        question_start = datetime.datetime.now()
        answer = input(question.text + ' = ')
        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()
        answer_time = (question_end - question_start).seconds
        self.answer_times.append(answer_time)
        
        return correct

    def total_correct(self):
        total_correct = 0
        for answer in self.answers:
            if answer == True:
                total_correct += 1
        return total_correct

    def summary(self):
        time_elapsed = (self.end_time-self.start_time).seconds
        print(f'You got {self.total_correct()}/{len(self.questions)} questions right')
        print(f'It took you {time_elapsed} seconds total')
        self.times.append(time_elapsed)
    
    def display_stats(self):
        i = 0
        for answer_time in self.answer_times:
            print(f'You took {answer_time} seconds to answer question {self.questions[i].text}')
            i+=1

   
custom_ops = input("""Welcome to the math quiz!
which operations would you like to have on your quiz?
1. Addition
2. Subtraction
3. Multiplication
4. Division
To choose enter the numbers of the desired operations
i.e. 1 2 3 = Addition, subtraction and multiplication
Enter Here ==>  """)

while True:
    try:

        num_questions = int(input("How many questions you would like to be tested on? "))
        num_range_low = int(input("""what range of numbers you would like to be tested on? 
Pick the lower end of the range: """))
        num_range_high = int(input("""Pick the Higher end of the range: """))
    
    except ValueError:
        print('Please enter whole integers')
        continue
    break

rerun = 'Y'
while rerun.upper() == 'Y':
    new_quiz = Quiz(custom_ops, num_questions, num_range_low, num_range_high)
    new_quiz.take_quiz()
    print(f'The high score is {min(new_quiz.times)} Seconds')
    display_stats = input('Would you like to see how long you have spend on each question? [Y/N] ')
    if display_stats.upper() == 'Y':
        new_quiz.display_stats()
    rerun = input('Retake Quiz? [Y/N] ')
    del new_quiz.questions [0:len(new_quiz.questions)]
    del new_quiz.answers [0:len(new_quiz.answers)]
    del new_quiz.answer_times [0:len(new_quiz.answer_times)]
