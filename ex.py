def troco(n):
    resultSet = set()  # cria um conjunto vazio para armazenar as representações de N centavos.
    
    # itera sobre o número de quarters (25 centavos) possíveis.
    for quarters in range(n // 25 + 1):
        # itera sobre o número de dimes (10 centavos) possíveis.
        for dimes in range(n // 10 + 1):
            # itera sobre o número de nickels (5 centavos) possíveis.
            for nickels in range(n // 5 + 1):
                # calcula o número de pennies (1 centavo) necessários para completar N centavos.
                pennies = n - quarters * 25 - dimes * 10 - nickels * 5
                # se o total de pennies (1 centavo) for maior ou igual a zero, adiciona ao conjunto.
                if pennies >= 0:
                    resultSet.add((quarters, dimes, nickels, pennies))
    
    return resultSet  # retorna todos os trocos possíveis com o numero dado pelo usuario.

# parte do input para o usuário inserir os centavos que deseja.
n = int(input("Quantos pennies/centavos deseja que seja calculado?"))
result = troco(n)
print("Os resultados possíveis de trocos são", result)
