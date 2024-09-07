from questions import Questions
from team import Team

#На вопросы тут пока что только заготовленные ответы

def main():

    num_teams = int(input("Введите количество команд (>1): "))
    teams = []

    for _ in range(num_teams):
        team_name = input("Введите название команды (<= 50 символов): ")
        teams.append(Team(team_name))

    questions = Questions()
    correct_answers = [q["answer"] for q in questions.questions_list]


    for question_data in questions.questions_list:
        print(question_data["question"])
        for team in teams:
            answer = input(f"{team.name}, ваш ответ: ")
            team.add_answer(answer)


    for team in teams:
        team.calculate_score(correct_answers)


    print("\nРезультаты:")
    for team in teams:
        print(f"{team.name}: {team.score} очков")

if __name__ == "__main__":
    main()
