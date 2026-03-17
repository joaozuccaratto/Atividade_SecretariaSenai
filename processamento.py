def top_estudante(alunos):
    top_nome = ""
    top_media = 0

    for nome, notas in alunos:
        if validar_notas(notas):
            media = calcular_media(notas)

            if media > top_media:
                top_media = media
                top_nome = nome

    return top_nome, top_media