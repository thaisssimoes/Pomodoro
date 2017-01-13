import win32api
import time
import signal


class Pomodoro():

    def on_exit(self, sig, func=None):
        print "exit handler"
    def alertaTrabalho(self):
        win32api.MessageBox(0, 'Seu horario de trabalho acabou!! Vai descansar!', "Free Pass \o/", 0x00001000)
        signal.signal(signal.SIGTERM, func=None)

    def alertaDescanso(self):
        win32api.MessageBox(0, "Seu horario de descanso acabou!! Vai trabalhar!", "Caminhao de trabalho", 0x00001000)
        signal.signal(signal.SIGTERM, func=None)


pomodoro = Pomodoro()
tempoDeDescanso = 0.1
tempoDeTrabalho = 0.1

while True:

    time.sleep(tempoDeTrabalho*60)
    pomodoro.alertaTrabalho()
    time.sleep(tempoDeDescanso * 60)
    pomodoro.alertaTrabalho()






