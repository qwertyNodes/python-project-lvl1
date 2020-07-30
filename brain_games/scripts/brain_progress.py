from brain_games import cli


def generate_progress_string(progress, rand_choose):
    progress_str = ''

    for num in progress:
        if num == progress[rand_choose]:
            progress_str += '.. '
            continue

        progress_str += '{} '.format(num)

    return progress_str


def ask_question(name):
    progress = cli.gen_progression()
    rand_choose = cli.gen_rand(1, min_=0, max_=len(progress) - 1)
    progress_str = generate_progress_string(progress, rand_choose)

    user_answ = cli.ask_something('Question: {}'.format(progress_str))

    try:
        if int(user_answ) == progress[rand_choose]:
            return True
    except ValueError:
        pass

    cli.incorrect_answer_print(user_answ, progress[rand_choose], name)
    return False


def main():
    cli.meet_user('What number is missing in the progression?')
    name = cli.get_name()
    count = 1

    while ask_question(name) and count < 3:
        count += 1

    if count == 3:
        cli.congrat_message(name)


if __name__ == '__main__':
    main()
