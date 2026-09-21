import pytest

from tech.angelofdiasg.qabank.operacoes.validar_transferencia_pix import validar_transferencia_pix


@pytest.mark.parametrize(
    "saldo_conta, valor_transferencia, conta_destino, limite_diario, horario_transferencia, resultado_esperado",
    [
        (1000, 200, "123456", 500, 14, "Aprovado"),
        (1000, 200, None, 500, 14, "Aprovado"),
        (100, 200, "123456", 500, 14, "Recusado"),
    ],
)
def test_validar_transferencia_pix(saldo_conta, valor_transferencia, conta_destino, limite_diario, horario_transferencia, resultado_esperado):
    resultado = validar_transferencia_pix(
        saldo_conta,
        valor_transferencia,
        conta_destino,
        limite_diario,
        horario_transferencia,
    )

    assert resultado == resultado_esperado
