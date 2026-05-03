from data import questions

def format_data(questions):
    data_q = questions['question']
    data_a = questions['a']
    data_b = questions['b']

    return f'{data_q}\na) {data_a}\nb) {data_b}'

def check_answer(answer, c_answer):
    return answer == c_answer

score = 0
lives = 5



for question in questions:
    print(format_data(question))
    guess = input('Type you answer "A" or "B" ?: ').lower()

    if check_answer(guess, question['answer']):
        score +=1
        print(f'\nCorrect. Score: {score}\n')
    else:
        lives -=1
        print(f'\nWrong. Lives left: {lives}\n')

    if lives == 0:
        print('You are out of lives.')
        break

print(f'Final score: {score}/{len(questions)}')