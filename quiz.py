class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "Which of the following elements is most abundant in Earth's crust?",
                "options": ["Oxygen", "Silicon", "Aluminum", "Iron"],
                "answer": "Oxygen"
            },
            {
                "question": "Who was the first woman to win a Nobel Prize?",
                "options": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Lise Meitner"],
                "answer": "Marie Curie"
            },
            {
                "question": "What is the longest river in the world?",
                "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
                "answer": "Amazon"
            },
            {
                "question": "What is the value of Pi to 4 decimal places?",
                "options": ["3.1415", "3.1416", "3.1420", "3.1400"],
                "answer": "3.1416"
            },
            {
                "question": "Which of the following countries does not have a border with India?",
                "options": ["China", "Bangladesh", "Nepal", "Thailand"],
                "answer": "Thailand"
            },
            {
                "question": "Who is the author of the book '1984'?",
                "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "F. Scott Fitzgerald"],
                "answer": "George Orwell"
            },
            {
                "question": "What is the capital city of Canada?",
                "options": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
                "answer": "Ottawa"
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": ["Diamond", "Gold", "Platinum", "Iron"],
                "answer": "Diamond"
            }
        ]
        self.score = 0

    def ask_question(self, question, options, correct_answer):
        print(question)
        # Show options
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        # Input validation
        user_answer = input("Enter the number corresponding to your answer: ")
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if 1 <= user_answer <= len(options):
                selected_option = options[user_answer - 1]
                if selected_option == correct_answer:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect! The correct answer is: {correct_answer}")
            else:
                print("Invalid choice, please select a valid option.")
        else:
            print("Invalid input. Please enter a number corresponding to an option.")

    def start_quiz(self):
        # Ask each question
        for q in self.questions:
            self.ask_question(q['question'], q['options'], q['answer'])
        
        # Display the final score
        print(f"\nQuiz complete! Your final score is: {self.score} out of {len(self.questions)}")

# Main function to run the quiz
def main():
    quiz = Quiz()
    print("Welcome to the Python Quiz!\n")
    quiz.start_quiz()

if __name__ == "__main__":
    main()
