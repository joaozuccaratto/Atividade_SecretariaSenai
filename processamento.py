def alunos_recuperacao(alunos):
    recuperacao = []

    for nome, notas in alunos:
        if validar_notas(notas):
            media = calcular_media(notas)

            if media < 7:
                recuperacao.append((nome, media))

    return recuperacao