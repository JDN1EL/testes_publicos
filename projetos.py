import random
#ns -> numero secreto, tt -> total de tentativas, r -> rodada, cstr -> chute_str, p -> pontos, pp -> pontos perdidos
print ('='*33,'\nBem vindo ao jogo de adivinhação\n','='*33)

ns = random.randrange (1,11)
tt = 0
p = 200
print ("Escolha a dificuldade:\n",ns)
print ("(1) Facil (2) Médio (3) Dificil")

nivel = int (input ('Defina o nivel: '))
print('.',('='*33),'.')

if (nivel == 1):
   tt = 20
if (nivel == 2):
   tt = 10
if (nivel == 3):
   tt = 5

for rodada in range (1, tt +1):
   print ("Tentativa {} de {}".format (rodada, tt))
   cstr = input ("Digite um número entre 1 e 10:\n")
   print ("Você digitou", cstr)
   chute = int(cstr)
   if (chute < 1 or chute > 11):
      print ("Você deve digitar um número entre 1 e 10!")
      continue
     
   acertou = chute == ns
   maior = chute > ns
   menor = chute < ns

   if (acertou):
      print ('Acertô miserávi!\n Total de pontos {}'.format(p))
      break
   else:
      if (maior):
         ('ERRADO, Seu chute foi maior que o secreto.')
      elif (menor):
         ('ERRADO, Seu chute foi menor que o secreto, que droga eim.')
         pp = ns - chute
         p = p - pp
print('Fim do jogo')
