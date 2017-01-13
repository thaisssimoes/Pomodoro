import win32api
import time

class Pomodoro():
    def alertaTrabalho(self):
            win32api.MessageBox(0, 'Seu horario de trabalho acabou!! Vai descansar!', "Free Pass \o/", 0x00001000)
    def alertaDescanso(self):
            win32api.MessageBox(0, "Seu horario de descanso acabou!! Vai trabalhar!", "Caminhao de trabalho", 0x00001000)


pomodoro = Pomodoro()
tempoDeDescanso = 5
tempoDeTrabalho = 25

while True:

    time.sleep(tempoDeTrabalho*60)
    pomodoro.alertaTrabalho()
    time.sleep(tempoDeDescanso * 60)
    pomodoro.alertaDescanso()


