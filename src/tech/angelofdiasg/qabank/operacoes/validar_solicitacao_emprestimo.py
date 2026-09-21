import math


def validar_solicitacao_emprestimo(
	idade,
	score_credito,
	salario_mensal,
	valor_solicitado,
	divida_mensal,
):
	"""Valida se uma solicitação de empréstimo pode ser aprovada."""
	dados = (
		idade,
		score_credito,
		salario_mensal,
		valor_solicitado,
		divida_mensal,
	)

	if any(
		not isinstance(dado, (int, float))
		or isinstance(dado, bool)
		or not math.isfinite(dado)
		for dado in dados
	):
		raise ValueError("Dados da solicitação inválidos")

	if idade < 18:
		raise ValueError("Menor de idade não permitido")

	if score_credito < 650:
		return "Recusado"

	if salario_mensal <= 0:
		return "Recusado"

	if valor_solicitado <= 0:
		return "Recusado"

	if valor_solicitado > salario_mensal * 10:
		return "Recusado"

	if divida_mensal > salario_mensal * 0.4:
		return "Recusado"

	return "Aprovado"