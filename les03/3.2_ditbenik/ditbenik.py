def main():
    questions = [
        {
            'question': 'Hoe oud ben ik?',
            'answers': {
                'a': '16',
                'b': '17',
                'c': '18'
            },
            'right_answer': 'a'
        },
        {
            'question': 'Waar kom ik vandaan?',
            'answers': {
                'a': 'Amsterdam',
                'b': 'Alkmaar',
                'c': 'Bergen'
            },
            'right_answer': 'b'
        },
        {
            'question': 'Hoe schrijf je mijn naam?',
            'answers': {
                'a': 'Youri',
                'b': 'Joerie',
                'c': 'Joeri'
            },
            'right_answer': 'c'
        },
        {
            'question': 'Welk nieveau heb ik hiervoor gedaan?',
            'answers': {
                'a': 'GYMNASIUM',
                'b': 'VWO',
                'c': 'HAVO'
            },
            'right_answer': 'c'
        }
    ]
    points = 0

    def check_input(input_question, input_key) -> bool:
        return input_question['right_answer'] == input_key.lower() or input_question['answers'][
            input_question['right_answer']].lower() == input_key.lower()

    for question in questions:
        print(question['question'])
        print(len(question['question']) * '-')

        for answer in question['answers']:
            print(f"{answer.upper()} - {question['answers'][answer]}")

        correct = check_input(question, input('>> '))
        if correct:
            print('Goed gedaan!')
            points += 1
        else:
            print('Je hebt het fout.')

    print(f"Je hebt {points} van de {len(questions)} vragen juist beantwoord.")
    percentage = 100 / len(questions) * points
    print(f"Dat is {percentage}% van de vragen goed beantwoord.")


if __name__ == '__main__':
    main()
