from brain_games import cli


def ask_question(name):
    num1, num2 = cli.gen_rand(2)
    calc_nod = cli.get_NOD(num1, num2)

    print('Question: {} {}'.format(num1, num2))
    user_ans = cli.get_answer()

    if int(user_ans) == calc_nod:
        return True

    cli.incorrect_answer_print(user_ans, calc_nod, name)
    return False


def main():
    game_description = 'Find the greatest common divisor of given numbers.'

    cli.meet_user(game_description)
    name = cli.get_name()

    count = 1
    while ask_question(name) and count < 3:
        count += 1

    if count == 3:
        cli.congrat_message(name)


if __name__ == '__main__':
    main()
