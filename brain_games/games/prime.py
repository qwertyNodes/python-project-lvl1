from brain_games.scripts import cli


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer_pair():
    num = cli.gen_rand(min_=3, max_=100)

    question = str(num)
    answer = 'yes' if cli.is_simple(num) else 'no'

    return question, answer
