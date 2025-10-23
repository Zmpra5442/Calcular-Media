
notas = [8.5, 9.0, 7.2, 5.0, 6.5, 10.0, 4.0, 8.8, 3.5, 7.8]

def calcular_media(lista_notas):
    if not lista_notas:
        return 0.0
    soma = sum(lista_notas)
    media = soma / len(lista_notas)
    return media

media_da_turma = calcular_media(notas)

print(f'A lista de notas é: {notas}')
print(f'A média da turma é: {media_da_turma: .2f}')

def encontrar_maior_nota(lista_notas):
    if not lista_notas:
        return None
    
    maior_nota = max(lista_notas)
    return maior_nota

maior_nota = encontrar_maior_nota(notas)
print(f'A maior nota da turma foi: {maior_nota}')
    
def contar_aprovados(lista_notas , nota_corte = 6.0):
    contador = 0
    for nota in lista_notas:
        if nota >= nota_corte:
            contador = contador + 1
    return contador

aprovados_padrao = contar_aprovados(notas)
print(f'Alunos aprovados (corte 6.0): {aprovados_padrao}')

        
        