alunos = []
dietas = {
    'perderpeso': {
        1 : 'Comer devagar e respeitar a saciedade do corpo. Comer devagar permite que o estômago saciado avise ao cérebro que já recebeu comida suficiente.',
        2 : 'Beber mais água durante o dia.',
        3 : 'Fazer algum exercício físico',
        4 : 'Comer de tudo, mas pouca quantidade.',
        5 : 'Evitar ficar com muita fome'

    },

    'ganharpeso': {
        1 : 'Aumentar a ingestão de líquidos no dia (mínimo de 2L de água)',
        2 : 'Diminuir o intervalo entre as refeições.',
        3 : 'Consumir alimentos saudáveis.',
        4 : 'Praticar exercícios físicos de quatro a cinco vezes por semana.',
        5 : 'Ter um bom período de sono (entre 7 e 8 horas de sono)'

    },
    'manterpeso' : {
        1 : 'Consuma alimentos fontes de proteínas magras',
        2 : 'Consuma alimentos fontes de carboidratos integrais',
        3 : ' Evite as gorduras ruins: saturada e trans, inclua alimentos fontes de gorduras saudáveis: abacate, azeite extra virgem, oleaginosas (castanha, amêndoa, noz), peixe',
        4 : 'Consuma açúcar e sal com moderação',
        5 : 'Aumente a ingestão de água nos intervalos das refeições'
    }
}
exercicios = {
    'leve' : {
        1 : 'Ponte 20 Segundos',
        2 : 'Agachamento na Cadeira',
        3 : 'Agachamento na Parede',
        4 : 'Aviãozinho'
    },

    'moderado' : {
        1 : 'Flexão de Braço (3 Séries de 10 Movimentos',
        2 : 'Abdominal (3 Séries de 30 Movimentos',
        3 : 'Remada (3 Séries de 10 a 12 Movimentos por Braço',
        4 : 'Elevação das pontas dos pés'
    },

    'avancado' : {
        1 : 'Pular Corda',
        2 : 'Corrida estacionaria',
        3 : 'Tríceps no banco',
        4 : 'Bicicleta imaginária'
    }
}

while True:
    print('=== MENU ===')
    print('1 - Cadastrar aluno\n2 - Consultar alunos\n3 - Consultar Dieta\n4 - Consultar Treino')
    menu = int(input('Digite a opção:  '))

    if(menu == 1):
        print('CADASTRO DE ALUNO')
        aluno = {
            'nome': input('Digite seu nome: '),
            'idade': int(input('Digite sua idade: ')),
            'sexo': input('Digite seu sexo - F ou M: '),
            'peso': float(input('Digite seu peso em KG: ')),
            'altura': int(input('Digite sua altura em Cm: ')) / 100,
            'nivel_atividade': int(input('Digite o nível de Atividade:\n0 - Sedentario\n1 - Leve\n2 - moderado\n3 - intenso\n4 - muito intenso\n'))
        }
        alunos.append(aluno)

        print('')

    elif(menu == 2):
        print('=== CONSULTA DE ALUNOS ===')
        nome = input('Digite o nome do aluno: ')
        for aluno in alunos:
            if(aluno['nome'] == nome):
                if (aluno['sexo'] == 'M'):
                    tmb = (10 * aluno['peso']) + (6.25 * aluno['altura']) - (5 * aluno['idade']) + 5
                else:
                    tmb = (10 * aluno['peso']) + (6.25 * aluno['altura']) - (5 * aluno['idade']) - 161
                print(aluno)
            else:
                print('nao encontrado')

        print('')

    elif(menu == 3):
        print('=== CONSULTA DE DIETA ===')
        nome = input('Digite o nome do Aluno: ')
        for aluno in alunos:
            if(aluno['nome'] == nome):
                imc = aluno['peso'] / (aluno['altura']**2)
                print(imc)
                if(imc < 18.5):
                    print(f'Abaixo do peso\nRecomendação:\n{dietas["ganharpeso"][1]}\n{dietas["ganharpeso"][2]}\n{dietas["ganharpeso"][3]}\n{dietas["ganharpeso"][4]}')
                elif(imc > 18.5 and imc <= 24.9):
                    print(f'Peso Ideal\nRecomendação:\n{dietas["manterpeso"][1]}\n{dietas["manterpeso"][2]}\n{dietas["manterpeso"][3]}\n{dietas["manterpeso"][4]}')
                elif(imc > 24.9 and imc <= 29.9):
                    print(f'Levemente acima do peso\nRecomendação:\n{dietas["perderpeso"][1]}\n{dietas["perderpeso"][2]}\n{dietas["perderpeso"][3]}\n{dietas["perderpeso"][4]}')
                elif(imc > 29.9 and imc <= 34.9):
                    print(f'Obesidade grau 1\nRecomendação:\n{dietas["perderpeso"][1]}\n{dietas["perderpeso"][2]}\n{dietas["perderpeso"][3]}\n{dietas["perderpeso"][4]}')
                elif(imc > 34.9 and imc <= 39.9):
                    print(f'Obsidade grau 2\nRecomendação:\n{dietas["perderpeso"][1]}\n{dietas["perderpeso"][2]}\n{dietas["perderpeso"][3]}\n{dietas["perderpeso"][4]}')
                else:
                    print(f'Obesidade Mórbida\nRecomendação:\n{dietas["perderpeso"][1]}\n{dietas["perderpeso"][2]}\n{dietas["perderpeso"][3]}\n{dietas["perderpeso"][4]}')
            else:
                print('Aluno não encontrado')

    elif(menu == 4):
        print('===Consultar Treino===')
        nome = input('Digite o nome do Aluno: ')
        for aluno in alunos:
            if (aluno['nome'] == nome):
                if (aluno['nivel_atividade'] == 0):
                    print(f'Sedentário\nRecomendação:\n{exercicios["leve"][1]}\n{exercicios["leve"][2]}\n{exercicios["leve"][3]}\n{exercicios["leve"][4]}')
                elif (aluno['nivel_atividade'] == 1):
                    print(f'Leve\nRecomendação:\n{exercicios["leve"][1]}\n{exercicios["leve"][2]}\n{exercicios["leve"][3]}\n{exercicios["leve"][4]}')
                elif (aluno['nivel_atividade'] == 2):
                    print(f'Moderado\nRecomendação\n{exercicios["moderado"][1]}\n{exercicios["moderado"][2]}\n{exercicios["moderado"][3]}\n{exercicios["moderado"][4]}')
                elif (aluno['nivel_atividade'] == 3):
                    print(f'Intenso\nRecomendação\n{exercicios["moderado"][1]}\n{exercicios["moderado"][2]}\n{exercicios["moderado"][3]}\n{exercicios["moderado"][4]}')
                elif (aluno['nivel_atividade'] == 4):
                    print(f'Muito Intenso\nRecomendação\n{exercicios["avancado"][1]}n{exercicios["avancado"][2]}n{exercicios["avancado"][3]}n{exercicios["avancado"][4]}')

            else:
                print('Aluno não encontrado')





