import PySimpleGUI as sg

#color in hex
bt = {'size':(10,2), 'font':('Franklin Gothic Book', 18), 'button_color':("white",'#df6b77')}

White = '#F8F8FF'
Black = '#000000'

sg.theme('DarkBlack')

def score() :

    layout =[ [sg.Text('ONE-TOUCH', size=(23,2), justification='center', text_color='White', font=('Franklin Gothic Book', 40, 'bold'))],
            [sg.Text('--------', size=(8, 2), font=('Segoe UI', 14), text_color='Black'),sg.Text('SCORE : ', size=(10, 2), font=('Segoe UI', 25), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='Black', key='score')],   
            [sg.Text('--------', size=(22, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('RESTART',**bt),sg.Text('--------', size=(5, 1), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , value = window.read()
        if button == "RESTART" or button == sg.WIN_CLOSED:
            break

    window.close()

score()