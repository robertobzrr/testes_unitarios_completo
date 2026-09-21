import pytest
from tech.angelofdiasg.qabank.operacoes.validar_abertura_conta import validar_abertura_conta

# Parametrize (@pytest.mark.parametrize)
# O que é: É uma tabela de dados (Data-Driven Testing). Você fornece uma lista de cenários diferentes.

# Qual o objetivo: Rodar a mesma função de teste múltiplas vezes, apenas trocando as variáveis de entrada.

# Quando usar:

#   Quando você tem uma Tabela de Decisão.

#   Quando precisa testar vários números em uma calculadora (Ex: 2+2, -5+3, 0+0).

#   Quando precisa testar várias idades no validador (Ex: 17, 18, 19).

# Como funciona: Se você passar 5 linhas no parametrize, o Pytest vai rodar o teste 5 vezes independentes.

@pytest.mark.parametrize("idade, score_credito, renda_mensal, valor_primeiro_deposito, possui_negativado, resultado_esperado", [
    (18, 600, 1500, 100, False, "Aprovado"),  # Cenário 1: Limites mínimos
    (25, 599, 2000, 100, False, "Recusado"),  # Cenário 2: Score abaixo do mínimo
    (30, 800, 0, 100, False, "Recusado"),     # Cenário 3: Sem renda mensal
    (30, 800, 2000, 0, False, "Recusado"),    # Cenário 4: Sem primeiro depósito
])
def test_validador_conta_retornos(
    idade,
    score_credito,
    renda_mensal,
    valor_primeiro_deposito,
    possui_negativado,
    resultado_esperado,
):
    """Testa os cenários que retornam 'Aprovado' ou 'Recusado'."""
    resultado = validar_abertura_conta(
        idade,
        score_credito,
        renda_mensal,
        valor_primeiro_deposito,
        possui_negativado,
    )
    assert resultado == resultado_esperado

@pytest.mark.parametrize("idade, score_credito, renda_mensal, valor_primeiro_deposito, possui_negativado", [
    (17, 800, 2000, 100, False),  # Cenário 5: Menor de idade
])
def test_validador_conta_excecoes(
    idade,
    score_credito,
    renda_mensal,
    valor_primeiro_deposito,
    possui_negativado,
):
    """Testa os cenários de exceção para menores de idade."""
    with pytest.raises(ValueError, match="Menor de idade não permitido"):
        validar_abertura_conta(
            idade,
            score_credito,
            renda_mensal,
            valor_primeiro_deposito,
            possui_negativado,
        )