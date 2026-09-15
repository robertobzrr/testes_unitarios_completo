def validar_transferencia_pix(
    saldo_conta,
    valor_transferencia,
    conta_destino,
    limite_diario,
    horario_transferencia
):
    """
    Regra de negócio do QaBank:
    - Saldo da conta deve ser suficiente para a transferência.
    - Valor da transferência deve ser maior que zero.
    - Conta de destino deve ser informada.
    - Transferência não pode exceder o limite diário.
    - Transferência só pode ocorrer em horário comercial.
    """

    if saldo_conta < valor_transferencia:
        return "Recusado"

    if valor_transferencia <= 0:
        return "Recusado"

    if valor_transferencia > limite_diario:
        return "Recusado"

    # Brecha intencional:
    # A validação da conta de destino e do horário de operação foi esquecida.
    return "Aprovado"