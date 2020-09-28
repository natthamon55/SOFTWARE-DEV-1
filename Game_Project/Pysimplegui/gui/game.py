import PySimpleGUI as sg

#color in hex
bt = {'size':(10,2), 'font':('Franklin Gothic Book', 18), 'button_color':("white",'#df6b77')}

White = '#F8F8FF'
Black = '#000000'

sg.theme('DarkBlack')

def game():
    layout =[ [sg.Text('TIME : ', size=(15, 3), font=('Segoe UI', 18), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='time')],
            [sg.Text('SCORE : ', size=(15, 3), font=('Segoe UI', 18), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='score'),sg.Text('------ ', size=(15, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('EXIT',**bt)]            
             ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , value = window.read()
        if button == "EXIT" or button == sg.WIN_CLOSED:
            break

    window.close()

game()
