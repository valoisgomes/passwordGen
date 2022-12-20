import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # layot
        sg.theme('DarkBlue2')
        layout = [
            [sg.Text('Site/Software', size=(11, 1)),
             sg.Input(key='site', size=(50, 1))],
            [sg.Text('E-mail/Usuário', size=(11, 1)),
             sg.Input(key='user', size=(50, 1))],
            [sg.Text('Adicionar Números?', size=(25, 1)),
             sg.Combo(values=list(['SIM', 'NÃO']), key='numbers', default_value='NÂO', size=(5, 1))],
            [sg.Text('Adicionar Letras Maiúsculas?', size=(25, 1)),
             sg.Combo(values=list(['SIM', 'NÃO']), key='upperCaseLetters', default_value='NÂO', size=(5, 1))],
            [sg.Text('Adicionar Caracteres Especiais?', size=(25, 1)),
             sg.Combo(values=list(['SIM', 'NÃO']), key='CaracEspeciais', default_value='NÂO', size=(5, 1))],
            [sg.Text('Quanidade de Caracteres', size=(25, 1)),
             sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(5, 1))],
            [sg.Output(size=(64, 10))],
            [sg.Button('Gerar Senha')]
        ]

        # Declarar Janela

        self.janela = sg.Window('Password Generatio', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                newPassword = self.gerarSenha(valores)
                print(newPassword)
                print('ADD Numeros? ' + valores['numbers'])
                print('ADD UpperCase? ' + valores['upperCaseLetters'])
                print('ADD Especiais? ' + valores['CaracEspeciais'])

                self.salvarPassword(newPassword, valores)

    def gerarSenha(self, valores):
        charList = 'abcdefghijklmnopqrstuvwxyz'
        numberList = '0123456789'
        upperCaseList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        especiaisList = '!@#$%&*'

        if valores['numbers'] == 'SIM':
            charList = charList + numberList
        if valores['upperCaseLetters'] == 'SIM':
            charList = charList + upperCaseList
        if valores['CaracEspeciais'] == 'SIM':
            charList = charList + especiaisList

        chars = random.choices(charList, k=int(valores['total_chars']))
        newPass = ''.join(chars)
        return newPass

    def salvarPassword(self, newPassword, valores):
        with open('senhas.txt', 'a', newline='\r\n') as arquivo:
            arquivo.write(
                f"Site: {valores['site']}, Usuario: {valores['user']}, Nova Senha: {newPassword}")

        print('Arquivo senha.txt salvo')


gen = PassGen()
gen.Iniciar()
