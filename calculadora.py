# Inicia um loop infinito para manter a calculadora funcionando até que o usuário escolha sair.
while True:
    # Exibe as opções de operações disponíveis para o usuário.
    print("\nEscolha uma operação (+, -, *, /) ou digite 'sair' para encerrar:")
    
    # Solicita ao usuário que escolha uma operação, removendo espaços extras e convertendo para minúsculas.
    operacao = input('Operação: ').strip().lower()
    
    # Verifica se o usuário digitou 'sair'. Se sim, encerra o programa.
    if operacao == 'sair':
        print('Calculadora encerrada. Até mais!')
        break  # Sai do loop while.
    
    # Verifica se a operação escolhida é uma das operações permitidas.
    if operacao in ('+', '-', '*', '/'):
        try:
            # Solicita ao usuário o primeiro número, removendo espaços extras e convertendo para minúsculas.
            num1 = input("Digite o primeiro número (ou 'sair' para encerrar): ").strip().lower()
            
            # Verifica se o usuário digitou 'sair'. Se sim, encerra o programa.
            if num1 == 'sair':
                print('Calculadora encerrada. Até mais!')
                break  # Sai do loop while.
            
            # Converte a entrada para float. Se falhar, gera uma exceção ValueError.
            num1 = float(num1)
            
            # Solicita ao usuário o segundo número, removendo espaços extras e convertendo para minúsculas.
            num2 = input("Digite o segundo número (ou 'sair' para encerrar): ").strip().lower()
            
            # Verifica se o usuário digitou 'sair'. Se sim, encerra o programa.
            if num2 == 'sair':
                print('Calculadora encerrada. Até mais!')
                break  # Sai do loop while.
            
            # Converte a entrada para float. Se falhar, gera uma exceção ValueError.
            num2 = float(num2)
        
        # Captura exceções caso ocorra um erro ao converter as entradas para float.
        except ValueError:
            print('Erro: Insira números válidos.')
            continue  # Retorna ao início do loop.
        
        # Realiza a operação correspondente com base na escolha do usuário.
        if operacao == '+':
            print('Resultado:', num1 + num2)  # Soma.
        elif operacao == '-':
            print('Resultado:', num1 - num2)  # Subtrai.
        elif operacao == '*':
            print('Resultado:', num1 * num2)  # Multiplica.
        elif operacao == '/': 
            print('Resultado:', num1 / num2 if num2 != 0 else 'Erro: Divisão por zero')# Divide, e verifica se não está dividindo por zero
    
    # Caso a operação digitada não seja válida, exibe uma mensagem de erro.
    else:
        print('Operação inválida. Tente novamente.')
