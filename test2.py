import json

with open("questions.json", "r") as file:
    data = json.load(file)
score = 0


for question in data:
    print(question['question'])
    for index, alternatives in enumerate(question['alternatives']):
        print(index+1, "-", alternatives)

    user_input = int(input("Your answer:"))
    question['user_choice'] = user_input
    if question['user_choice'] == question['correct_answer']:
        score += 1

for index, question in enumerate(data):
    message =   f'Your asnser for {index+1} was {question["user_choice"]} ' \
                f'\nCorrect answer is {question["correct_answer"]}\n'

    print(message)
print(f'Your score is {score} of {len(data)}')
