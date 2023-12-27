class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        
    # Display a question and its options
    def display_question(self, question_num):
        question = self.questions[question_num]['question']
        options = self.questions[question_num]['options']
        print(f"\nQ{question_num + 1}: {question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        return len(options)

    # Checking if the user selected answer is correct or not
    def check_answer(self, question_num, user_answer):
        correct_answer = self.questions[question_num]['answer']
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
    
    def quiz_conduct(self):
        num_questions = len(self.questions)
        for i in range(num_questions):
            num_options = self.display_question(i)
            user_input = input(f"Enter your answer (1-{num_options}): ")
            # Validating user input
            while not user_input.isdigit() or int(user_input) not in range(1, num_options + 1):
                user_input = input(f"Invalid input. Please enter a number between 1 and {num_options}: ")
            self.check_answer(i, self.questions[i]['options'][int(user_input) - 1])

    # Display the final score
    def result(self):
        print(f"\nQuiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")


# Giving input data of questions,options and answers
quiz_data = [
    {
    "question":"who is the first prime minister of india ?",
    "options":["Gandhi","Nehru","Bhagath singh","Pranab Mukharji"],
    "answer":"Nehru"},
    
    {"question":"What is 10-8?",
    "options":["2","24","18","16"],
    "answer":"2"},
    
    {"question":"How many composite are there between 1 and 10?",
    "options":["2","3","4","1"],
    "answer":"4"}
]

# Creating a object named as Quiz with the above data provided
quiz = Quiz(quiz_data)

# Conducting the quiz
quiz.quiz_conduct()

# Displaying the result
quiz.result()
'''
At First i didnt have minimum knowledge abouut python but after learning from the w3 schools 
I have learnt how to answer any question in python language
The code will display the questions and options 
choose one option from the given nuumbering given to the options.
The final score is displayed.

'''
