from processamento import calcular_media, validar_notas, alunos_recuperacao, top_student, gerar_relatorio

alunos = [
    ("Ana", [8, 9, 7]),
    ("Pedro", [5, 6]),
    ("Carlos", [10, 9, 10]),
    ("Julia", [6, 7, 5]),
    ("Marcos", [7, 7, 7]),
    ("Fernanda", [9, 8, 9]),
    ("Lucas", [])
]

recuperacao = alunos_recuperacao(alunos)

melhor_aluno = top_student(alunos)

gerar_relatorio(alunos, recuperacao, melhor_aluno)

print("Programa finalizado!")

alunos = [
    ("Ana", [8, 9, 7]),
    ("Pedro", [5, 6]),
    ("Lucas", []),
    ("Julia", [6, 6]),
    ("Carlos", [10, 9]),
    ("Marina", [7, 7]),
    ("João", [4, 5])
]

recuperacao = alunos_recuperacao(alunos)
top_nome, top_media = top_estudante(alunos)

arquivo = open("relatorio.txt", "w")

arquivo.write("=== RELATÓRIO DE DESEMPENHO ===\n\n")

arquivo.write("Alunos em recuperação:\n")
for nome, media in recuperacao:
    arquivo.write(f"{nome} - Média: {media}\n")

arquivo.write("\nTop estudante:\n")
arquivo.write(f"{top_nome} - Média: {top_media}\n")

arquivo.close()

print("Relatório gerado com sucesso!")