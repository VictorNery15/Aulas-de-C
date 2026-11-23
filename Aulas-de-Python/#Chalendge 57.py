s = input('Digite seu sexo (M/F): ').strip().lower()[0]
while not s in 'mf':
        s = input('Error!! Escolha apenas entre as opções (M/F): ').strip().lower()
print(f"Sexo {s} resgitrado.")
