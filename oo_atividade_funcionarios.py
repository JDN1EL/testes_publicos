#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Crie uma super classe RelogioDePonto, uma subclasse Funcionarios e uma sub-subclasse Operador e Repositor:

# trabalhe com os atributos: hora_entrada, hora_saida, nome, matricula, expediente, ocorrencia 
# todos atributos encapsulados OK

# defina uma correta dsitribuição dos atributos entre as classes
# defina as nomenclaturas dos metodos e com base na explicação abaixo faça:
# você deve fazer os funcionários registrem a entrada e a saida com base no seu expediente
# você informar caso ele entre atrasado ou saia adiantado e mostrar quanto foi esse atraso ou adiantamento
# caso o atraso seja maior que 10 minutos registre uma ocorrencia

# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Faça a impressão dos elementos corretamente

from datetime import *#importei logo tudo kkkjkkkjk
class RelogioDePonto():
    def __init__(self):
        self.hora_entrada = 6#pode ser usado no lugar de parametros no meu codigo
        self.hora_saida = 10
        self.expediente = 6#parametro inicial para a noite
        self.__ocorrencia = 0
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @property
    def entrando(self):
        hora = int(input('Entrada\nDigite a hora e depois os minutos\nHORA de chegada: '))
        
        if hora == (self.expediente - 1):
            dez_minutos_atrasado = int(input('MINUTOS: '))
            if dez_minutos_atrasado >= 51:
                print(f'São {timedelta(hours= hora,minutes= dez_minutos_atrasado)}')
            else:
                print(f'Chegou atrasado são {timedelta(hours= hora,minutes= dez_minutos_atrasado)} levou ocorrência.')
        else:
            minutos = int(input('MINUTOS: '))
            if hora == self.expediente and minutos == 0:
                print(f'São {timedelta(hours= hora,minutes= minutos)}, bem vindo')
            else:
                self.__ocorrencia += 1
                print(f'Atrasou eim! são: {timedelta(hours= hora,minutes= minutos)}')
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    @property
    def saindo(self):
        hora_saida = int(input('\nSaida\nDigite a hora e depois os minutos\nHORA de saida: '))
        
        if hora_saida == (self.hora_saida - 1):
            dez_minutos_atrasado = int(input('MINUTOS: '))
            if dez_minutos_atrasado >= 51:
                print(f'São {timedelta(hours= hora_saida,minutes= dez_minutos_atrasado)}')
            else:
                self.__ocorrencia += 1
                print(f'Não tô segurando ninguém mas ja sabe né.. são: {timedelta(hours= hora_saida,minutes= dez_minutos_atrasado)}')
        else:
            minutos = int(input('MINUTOS: '))
            if hora_saida ==  self.hora_saida and minutos == 0:
                print(f'São {timedelta(hours= hora_saida,minutes= minutos)}, Tchau!')
            else:
                self.__ocorrencia += 1
                print(f'Atrasou eim! são: {timedelta(hours= hora_saida,minutes= minutos)}')
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @property
    def horarios(self):#opcional
        turnos = int(input('\nEscolha um turno..\n(1) De 2 às 5\n(2) De 6 às 10\n'))
        if turnos == 1:
            self.hora_entrada = 1
            self.hora_saida = 5
            self.expediente = 1
        if turnos == 2:
            self.hora_entrada = 6
            self.hora_saida = 10
            self.expediente = 6
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @property
    def ver_ocorrencia(self):
        return print(f'Total de ocorrencias registradas: {self.__ocorrencia}')
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Funcionarios(RelogioDePonto):
    def __init__(self,nome, matricula):
        super().__init__()
        self.__nome = nome.title()
        self.__matricula = matricula
    
    @property
    def user_id(self):
        return self.__matricula

    @user_id.setter
    def user_id(self,id):
        if type(id) == type(str()):
            self.__matricula = id
        else:
            print("Deve ser STRING!")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         
    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if type(novo_nome) == type(str()):
            self.__nome = novo_nome
        else:
            print("Nome deve ser STRING!")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
class Operador(Funcionarios):  
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Repositor(Funcionarios):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    

# registros = Funcionarios('David','daidvd@valley.com')
# print(registros.get_nome())
# print(registros.user_id)
# registros.entrando
# registros.saindo
# registros.ver_ocorrencia
#============================================================================================================================================================================================
# registros2 = Operador('Mihawk','0002006')
# print(registros2.get_nome())
# print(registros2.user_id)
# registros2.entrando
# registros2.saindo
# registros2.ver_ocorrencia
##============================================================================================================================================================================================
cara_que_ajeita_as_caixas_la_sei_la = Repositor('ichigo','0001500010')
print(cara_que_ajeita_as_caixas_la_sei_la.get_nome())
print(cara_que_ajeita_as_caixas_la_sei_la.user_id)
cara_que_ajeita_as_caixas_la_sei_la.entrando
cara_que_ajeita_as_caixas_la_sei_la.saindo
cara_que_ajeita_as_caixas_la_sei_la.ver_ocorrencia
