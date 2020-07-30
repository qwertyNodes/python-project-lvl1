from brain_games import cli


def ask_question(name):
    num = cli.gen_rand(1, min_=3, max_=100)

    calc_answer = cli.is_simple(num)
    user_answer = cli.ask_something('Question: is this num simple: {} '
                                    '(yes/no)? '.format(num))

    if (calc_answer and user_answer.lower() == 'yes') or \
            (not calc_answer and user_answer.lower() == 'no'):
        return True

    cli.incorrect_answer_print(user_answer, 'yes' if calc_answer else 'no', name)
    return False


def main():
    cli.meet_user('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = cli.get_name()

    count = 1
    while ask_question(name) and count < 3:
        count += 1

    if count == 3:
        cli.congrat_message(name)


if __name__ == '__main__':
    main()
