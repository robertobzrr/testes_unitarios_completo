# Crie uma função chamada validar_solicitacao_emprestimo que valide se uma solicitação de empréstimo pode ser aprovada no QaBank.

# Regra de negócio:

# O cliente deve ter pelo menos 18 anos.
# O score de crédito deve ser maior ou igual a 650.
# O salário mensal deve ser maior que zero.
# O valor solicitado deve ser maior que zero.
# O valor solicitado não pode ultrapassar 10 vezes o salário mensal.
# A dívida mensal não pode comprometer mais de 40% da renda do cliente.
# Se o cliente for menor de idade, a função deve lançar exceção.
# Se qualquer dado obrigatório estiver ausente, nulo ou em formato inválido, a função deve tratar como erro de entrada.
# Se o score for insuficiente, o salário for inválido, o valor do empréstimo for inválido, ou a dívida comprometer mais de 40% da renda, o resultado deve ser "Recusado".
# Se todas as condições forem atendidas, o resultado deve ser "Aprovado".


# Critérios de aceitação:

# Menor de 18 anos → exceção
# Score abaixo de 650 → "Recusado"
# Salário menor ou igual a zero → "Recusado"
# Valor do empréstimo menor ou igual a zero → "Recusado"
# Valor do empréstimo acima de 10x o salário → "Recusado"
# Dívida mensal acima de 40% da renda → "Recusado"
# Dados inválidos ou ausentes → erro de validação
# Tudo válido → "Aprovado"