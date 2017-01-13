import win32api
import time

class Pomodoro():
    def __init__(self):
        self.now = time.localtime(time.time())
    def trabalho(self, tempoTrabalho):
        self.minutoAtual = self.now.tm_min
        self.minutoTrabalhoFinal = self.minutoAtual + tempoTrabalho
        if self.minutoTrabalhoFinal >= 60:
            self.minutoTrabalhoFinal= self.minutoTrabalhoFinal - 60
            self.horaAtual= self.now.tm_hour+1
        else:
            self.horaAtual = self.now.tm_hour
    def descanso(self, tempoDescanso):
        self.minutoAtual = self.now.tm_min
        self.minutoDescansoFinal = self.minutoAtual + tempoDescanso
        if self.minutoDescansoFinal>= 60:
            self.minutoDescansoFinal= self.minutoDescansoFinal - 60
            self.horaAtual= self.now.tm_hour+1
        else:
            self.horaAtual = self.now.tm_hour
    def alertaTrabalho(self):
        if self.now.tm_hour == self.horaAtual and self.now.tm_min == self.minutoTrabalhoFinal:
            win32api.MessageBox(0, 'Seu horario de trabalho acabou!! Vai descansar!', "title", 0x00001000)
    def alertaDescanso(self):
        if self.now.tm_hour == self.horaAtual and self.now.tm_min == self.minutoDescansoFinal:
            win32api.MessageBox(0, "Seu horario de descanso acabou!!", "title", 0x00001000)


pomodoro = Pomodoro()
tempoDeDescanso = 0
tempoDeTrabalho = 1

while True:
    pomodoro.trabalho(tempoDeTrabalho)
    pomodoro.alertaTrabalho()
    pomodoro.descanso(tempoDeDescanso)
    #elif pomodoro.descanso(tempoDeDescanso):
    #    pomodoro.alertaDescanso()
     #   pomodoro.trabalho(tempoDeTrabalho)

