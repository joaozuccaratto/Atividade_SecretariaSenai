from processamento import calcular_media, validar_notas, alunos_recuperacao, top_student, gerar_relatorio

alunos = [
    ("Ana", [8, 9, 7]),
    ("Pedro", [5, 6]),
    ("Carlos", [6, 9, 8]),
    ("Julia", [5, 7, 5]),
    ("Marcos", [7, 7, 6]),
    ("Fernanda", [9, 8, 9]),
    ("Lucas", [])
]
recuperacao = alunos_recuperacao
melhor_aluno = top_student(alunos)

relarotio = gerar_relatorio(alunos)

