import pytest

from tech.angelofdiasg.qabank.operacoes.validar_solicitacao_emprestimo import (
    validar_solicitacao_emprestimo,
)


@pytest.mark.parametrize(
    "idade, score_credito, salario_mensal, valor_solicitado, divida_mensal, resultado_esperado",
    [
        (30, 700, 5000, 10000, 1000, "Aprovado"),
        (30, 649, 5000, 10000, 1000, "Recusado"),
        (30, 700, 0, 10000, 1000, "Recusado"),
        (30, 700, 5000, 0, 1000, "Recusado"),
        (30, 700, 5000, 50001, 1000, "Recusado"),
        (30, 700, 5000, 10000, 2001, "Recusado"),
    ],
)
def test_validar_solicitacao_emprestimo_retornos(
    idade,
    score_credito,
    salario_mensal,
    valor_solicitado,
    divida_mensal,
    resultado_esperado,
):
    resultado = validar_solicitacao_emprestimo(
        idade,
        score_credito,
        salario_mensal,
        valor_solicitado,
        divida_mensal,
    )

    assert resultado == resultado_esperado


@pytest.mark.parametrize(
    "idade, score_credito, salario_mensal, valor_solicitado, divida_mensal",
    [
        (17, 700, 5000, 10000, 1000),
        (30, None, 5000, 10000, 1000),
        (30, 700, "5000", 10000, 1000),
        (30, float("nan"), 5000, 10000, 1000),
    ],
)
def test_validar_solicitacao_emprestimo_erros_de_validacao(
    idade,
    score_credito,
    salario_mensal,
    valor_solicitado,
    divida_mensal,
):
    with pytest.raises(ValueError):
        validar_solicitacao_emprestimo(
            idade,
            score_credito,
            salario_mensal,
            valor_solicitado,
            divida_mensal,
        )
