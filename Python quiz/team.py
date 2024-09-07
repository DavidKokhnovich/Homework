class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)

    def calculate_score(self, correct_answers):
        for answer, correct in zip(self.answers, correct_answers):
            if answer.strip().lower() == correct.strip().lower():
                self.score += 1
