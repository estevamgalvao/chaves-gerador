import random
print("Insira o nome dos participantes, um por vez, então digite -fim-.")
lista_participantes = []
participante_verif = 'inicio'
j = 0


while(participante_verif!='fim'):
    participante = input()
    lista_participantes.append(participante)
    participante_verif = participante.lower()

#lista_participantes.remove('fim')
lista_participantes = lista_participantes[:-1]
num_participantes = len(lista_participantes)
print('')

if (num_participantes%2!=0):
    print("O número de participantes que você inseriu não faz chaves corretas!")
    print("Insira outro participante para continuar.")
    participante = input()
    lista_participantes.append(participante)
    print("")

#print(num_participantes)
#print('lista:', lista_participantes)

while(j < num_participantes/2):
    selecionado1 = random.choice(lista_participantes)
    lista_participantes.remove(selecionado1)
    tamanho1 = len(selecionado1)
    selecionado2 = random.choice(lista_participantes)
    lista_participantes.remove(selecionado2)
    tamanho2 = len(selecionado2)
    j+=1
    print('*'*(tamanho1+8))
    print('*   %s   *' % (selecionado1))
    print('*'*(tamanho1+8))
    #print('',end = '')

    print("VERSUS")

    print('*' * (tamanho2+8))
    print('*   %s   *' % (selecionado2))
    print('*' * (tamanho2+8))
    print('')
    print('')
