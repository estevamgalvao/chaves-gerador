import random

print("Insira o nome dos participantes, um por vez, então digite -fim-.")

lista_participantes = [] #criando uma lista vazia. lista principal do código
lista_trapaca1 = []
lista_trapaca2 = []
confirmacao = 'nao' #começando a variável com valor para conseguir fazer comparações
participante_verif = 'inicio' #começando a variável com valor para conseguir fazer comparações
j = 0 #verifica while de prints dos brackets
k = 0 #auxilia o while pra conferir se o usuário digitou uma confirmação válida (sim ou n)
l = 0 #verifica o while se o usuário quer continuar inserindo novos brackets
ll = 0
lll = 0 #auxilia o while pra conferir se o usuário digitou uma confirmação válida (sim ou n)

opcao_cheat = 0

while(confirmacao=='nao' or confirmacao=='n' or confirmacao=='não'): #while-loop para manter o usuário enquanto n confirmar que quer parar de inscrever participantes
    while(participante_verif!='fim'):#while-loop para manter o programa pedindo nomes até 'fim'
        participante = input()
        lista_participantes.append(participante)
        participante_verif = participante.lower()

    while(k == 0):#manter o usuário no loop "tem certeza?"
        print("Tem certeza que deseja terminar de inscrever participantes?")
        confirmacao = input()
        confirmacao = confirmacao.lower()
        print("")
        if (confirmacao == 's' or confirmacao == 'sim'):
            k = 1
        elif (confirmacao == 'cheats on'):
            k = 1
            print("Selecione a trapaça:")
            print("[1] Quem contra quem;")

            opcao_cheat = int(input())
            if (opcao_cheat == 1):
                while(l==0):
                    #os whiles a seguir verificam se o participante foi inserido
                    while(ll==0):
                        cheat_selecionado1 = input("Participante: ")
                        count_lista = lista_participantes.count(cheat_selecionado1)
                        ll = 1
                        if (count_lista == 0):
                            print("Participante inválido.")
                            ll = 0

                    while(ll==1):
                        cheat_selecionado2 = input("Adversário: ")
                        count_lista = lista_participantes.count(cheat_selecionado1)
                        ll = 0
                        if (count_lista == 0):
                            print("Participante inválido.")
                            ll = 1

                    lista_participantes.remove(cheat_selecionado1)
                    lista_trapaca1.append(cheat_selecionado1)
                    lista_participantes.remove(cheat_selecionado2)
                    lista_trapaca2.append(cheat_selecionado2)

                    #estou atribuindo os nomes retirados a 2 listas paralalelas a fim de trabalhar com as 2 usando o mesmo índices e dessa forma, criando os pares trapaceados
                    tamanho1 = len(cheat_selecionado1)
                    tamanho2 = len(cheat_selecionado2)
                    ll = 0

                    while(lll==0):#manter usuário no loop do "continuar?"
                        print("Continuar?")
                        confirmacao2 = input()
                        confirmacao2 = confirmacao2.lower()
                        if (confirmacao2 == 's' or confirmacao2 == 'sim'):
                            lll = 1
                        elif (confirmacao2=='nao' or confirmacao2=='n' or confirmacao2=='não'):
                            l = 1
                            lll = 1
                        else:
                            print("Resposta inválida.")
                            print("")
        else:
            print("Resposta inválida.")




#lista_participantes.remove('fim')
lista_participantes = lista_participantes[:-1]
num_participantes = len(lista_participantes)

#print("LISTA PARTICIPANTES:", lista_participantes[0])
#lista_participantes.sort()
#print("LISTA PARTICIPANTES:", lista_participantes)
#print('')

if (num_participantes%2!=0):
    print("O número de participantes que você inseriu não faz chaves corretas!")
    print("Insira outro participante para continuar.")
    participante = input()
    lista_participantes.append(participante)
    print("")

#print(num_participantes)
#print('lista:', lista_participantes)

#print("")
#print("LISTA PARTICIPANTES: ", lista_participantes)
#print("")
#print("LISTA TRAPAÇA 1: ", lista_trapaca1)
#print("")
#print("LISTA TRAPAÇA 2: ", lista_trapaca2)
#tamanho1 = len(lista_trapaca1[0])
#print("TAMANHO1", tamanho1)
#print("INDICE_LISTA", indice_lista)
#input()


while(j < num_participantes/2):
    #print("PASSOU AQUI WHILE")
    if(opcao_cheat==1):
        for i in range(len(lista_trapaca1)):
            
            tamanho1 = len(lista_trapaca1[i])
            tamanho2 = len(lista_trapaca2[i])

            print('*' * (tamanho1 + 8))
            print('*   %s   *' % (lista_trapaca1[i]))
            print('*' * (tamanho1 + 8))
            # print('',end = '')

            print("VERSUS")

            print('*' * (tamanho2 + 8))
            print('*   %s   *' % (lista_trapaca2[i]))
            print('*' * (tamanho2 + 8))
            print('')
            print('')

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
    print("VERSUS")
    print('*' * (tamanho2+8))
    print('*   %s   *' % (selecionado2))
    print('*' * (tamanho2+8))
    print('')
    print('')
