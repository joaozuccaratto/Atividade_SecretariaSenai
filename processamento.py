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
