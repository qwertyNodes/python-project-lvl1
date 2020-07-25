import random

import prompt


def is_even(num):
    return num % 2 == 0


def ask_name():
    return prompt.string('May i have your name ?')


def ask_answer():
    ans = prompt.string('Your answer(yes/no): ')
    return 1 if ans == 'yes' else 0


def start_game(name):
    counter = 1
    while counter <= 3:
        rand_num = random.randrange(1, 100)
        print('Question: {}'.format(rand_num))

        answer = ask_answer()
        if is_even(rand_num) == answer:
            print('Correct!')
            counter += 1
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}"'
                  'Let\'s try again, {}!'.format(get_word_answ(answer), get_word_answ(not answer), name))
            return
    print('Congratulations, {}!'.format(name))


def get_word_answ(ans):
    return 'yes' if ans == 1 else 'no'


def main():
    print('Welcome to the Brain Games!\n'
          'Answer "yes" if number even otherwise answer "no".\n')

    name = ask_name()
    start_game(name)

    print('\nEXIT GAME!')


if __name__ == '__main__':
    main()



