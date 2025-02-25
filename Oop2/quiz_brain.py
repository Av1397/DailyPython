class QuizBrain:

    def __init__(self, question_list):

        self.number = 0
        self.score = 0
        self.question_list = question_list


    def still_has_questions(self):
        """Returns true if there are still questions left in question_list else false"""

        end = self.number
        return end < len(self.question_list)
    

    def next_question(self):

        current_question = self.question_list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number} {current_question.text} True/False: ")
        self.check_answer(user_answer, current_question.answer)
        

    
    def check_answer(self, user_answer, correct_answer):

        """Returns the final score"""
        if user_answer.lower() == correct_answer.lower():

            
            self.score += 1
            print("You got it correct!")

        else:

            print("Sorry! Wrong answer")

        print(f"The current answer is {correct_answer}")
        print(f"Your final score {self.score}/{self.number}")
        print("\n")

        
    


    