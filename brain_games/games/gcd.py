from brain_games.scripts import cli


description = 'Find the greatest common divisor of given numbers.'


def generate_question_answer_pair():
    num1, num2 = cli.gen_rand(2)

    question = '{} {}'.format(num1, num2)
    answer = str(cli.get_NOD(num1, num2))

    return question, answer
