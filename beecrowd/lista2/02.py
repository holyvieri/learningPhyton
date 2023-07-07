numbers = input().split()
scores = [float(num) for num in numbers]
average = ((scores[0]*2) + (scores[1]*3) + (scores[2]*4) + scores[3]) / 10
print(f'Media: {average:.1f}')

if average >= 7.0:
    print('Aluno aprovado.')
elif average < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exam_score = float(input())
    new_average = (average + exam_score) / 2

    print(f'Nota do exame: {exam_score:.1f}')

    if new_average >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {new_average:.1f}')
