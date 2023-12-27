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
    
    def conduct_quiz(self):
        num_questions = len(self.questions)
        for i in range(num_questions):
            num_options = self.display_question(i)
            user_input = input(f"Enter your answer (1-{num_options}): ")
            # Validating user input
            while not user_input.isdigit() or int(user_input) not in range(1, num_options + 1):
                user_input = input(f"Invalid input. Please enter a number between 1 and {num_options}: ")
            self.check_answer(i, self.questions[i]['options'][int(user_input) - 1])

    # Display the final score
    def show_result(self):
        print(f"\nQuiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")


# Giving input data of questions,options and answers
quiz_data = [
    {
    "question":"What is capital of India?",
    "options":["Mumbai","Delhi","Chennai","Gujarat"],
    "answer":"Delhi"},
    
    {"question":"What is 10+8?",
    "options":["20","24","18","16"],
    "answer":"18"},
    
    {"question":"How many primes are there between 1 and 10?",
    "options":["2","3","4","1"],
    "answer":"4"}
]

# Creating a object named as Quiz with the above data provided
my_quiz = Quiz(quiz_data)

# Conducting the quiz
my_quiz.conduct_quiz()

# Displaying the result
my_quiz.show_result()
'''
This code consists of functions,classes.
At first to design this I don’t know about classes in python. Later I learnt them from W3 schools and chatgpt.
With the help of W3 schools and chatgpt I can complete the code.
This code displays the question and options.
Next, we have choose one number from the numbering given to the options.
Then the input is validated. After the completion of all questions.
The final score is displayed.
'''