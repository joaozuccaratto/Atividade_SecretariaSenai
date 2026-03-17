def validar_notas(notas):
    if type(notas) != list:
        return False

    if len(notas) == 0:
        return False

    for nota in notas:
        if type(nota) != int and type(nota) != float:
            return False

    return True

  
def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma = soma + nota

    media = soma / len(notas)

    return media

  
def alunos_recuperacao(alunos):
    recuperacao = []

    for nome, notas in alunos:
        if validar_notas(notas):
            media = calcular_media(notas)
            if media < 7:
                recuperacao.append((nome, media))

    return recuperacao


def top_student(alunos):
    top_nome = ""
    top_media = 0

    for nome, notas in alunos:
        if validar_notas(notas):
            media = calcular_media(notas)

            if media > top_media:
                top_media = media
                top_nome = nome

    return top_nome, top_media


def gerar_relatorio(alunos):
    recuperacao = alunos_recuperacao(alunos)
    melhor = top_student(alunos)
    
    relatorio = "===== RELATÓRIO DE ALUNOS =====\n\n"
    relatorio += "Alunos em recuperação:\n"
    
    if recuperacao:
        for nome, media in recuperacao:
            relatorio += f"- {nome}: média {media:.2f}\n"
    else:
        relatorio += "Nenhum aluno em recuperação.\n"
    
    relatorio += "\nMelhor aluno:\n"
    relatorio += f"- {melhor[0]}: média {melhor[1]:.2f}\n"

    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
        print("Relatório gerado e salvo em 'resultado.txt' ✅")

    return relatorio