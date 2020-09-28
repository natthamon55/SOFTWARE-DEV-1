import PySimpleGUI as sg
import os

#color in hex
bt = {'size':(12,3), 'font':('Franklin Gothic Book', 18), 'button_color':("white",'#df6b77')}

White = '#F8F8FF'
Black = '#000000'

sg.theme('DarkBlack')


def main_menu() :

    layout =[ [sg.Text('ONE-TOUCH', size=(23,2), justification='center', text_color='White', font=('Franklin Gothic Book', 40, 'bold'))],
            [sg.Text('--------', size=(5, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('START',**bt),sg.Text('--------', size=(18, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('HOW TO PLAY ?',**bt)]    
            

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , value = window.read()
        if button == "START" or button == sg.WIN_CLOSED:
            break
        if button == "HOW TO PLAY ?" :
            sg.popup('Touch/Click the ball through the camera , When you tap it there will show your score with coundown timer :P')
       
    window.close()

main_menu()