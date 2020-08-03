from brain_games.scripts import cli


description = 'Answer "yes" if number even otherwise answer "no".'


def generate_question_answer_pair():
    rand_num = cli.gen_rand(max_=150)

    question = str(rand_num)
    correct_answer = 'yes' if rand_num % 2 == 0 else 'no'

    return question, correct_answer
