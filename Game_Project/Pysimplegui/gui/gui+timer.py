import PySimpleGUI as sg
from time import time

#color in hex
bt1 = {'size':(12,3), 'font':('Franklin Gothic Book', 18), 'button_color':("white",'#df6b77')}
bt2 = {'size':(10,2), 'font':('Franklin Gothic Book', 18), 'button_color':("white",'#df6b77')}

White = '#F8F8FF'
Black = '#000000'

sg.theme('DarkBlack')


def main_menu() :
    
    layout =[ 
            
            [sg.Text('ONE-TOUCH', size=(20,1), justification='center', text_color='White', font=('Franklin Gothic Book', 50, 'bold'))],
            [sg.Text('--------', size=(22, 2), font=('Segoe UI', 14), text_color='Black')],
            [sg.Text('--------', size=(10, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('START',**bt1),sg.Text('--------', size=(12, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('HOW TO PLAY ?',**bt1)] ,  
            [sg.Text('--------', size=(22, 2), font=('Segoe UI', 14), text_color='Black')]
            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , values = window.read()
        if button == "START" :
            game()

        if button == "HOW TO PLAY ?" :
            sg.popup('Touch/Click the ball through the camera , When you tap it there will show your score with coundown timer :P')

        if button == sg.WIN_CLOSED :
            break

    window.close()

def game():
    layout =[

            [sg.Button('TIME :',**bt2),sg.Text('', size=(10, 1), font=('Helvetica', 20),text_color = 'White',key='timer')],
            [sg.Text('SCORE : ', size=(15, 3), font=('Segoe UI', 18), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='score')]            
             
            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)
    while True:
        button, values = window.read()

        if button == sg.WIN_CLOSED :
            break

        if button == 'TIME :'  :
            seconds = 5
            start = time()
            current = time()
            timeleft = seconds

            while timeleft > 0 :
                window.FindElement("timer").Update(timeleft)
                window.refresh()
                current = time()
                timeleft = int(seconds - (current - start))
                if timeleft == 0:
                    sg.popup("TIME UP!")
                    score()


    window.close()



def score() :
    
    layout =[

            [sg.Text('ONE-TOUCH', size=(23,2), justification='center', text_color='White', font=('Franklin Gothic Book', 40, 'bold'))],
            [sg.Text('--------', size=(8, 2), font=('Segoe UI', 14), text_color='Black'),sg.Text('SCORE : ', size=(10, 2), font=('Segoe UI', 25), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='score')],   
            [sg.Text('--------', size=(22, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('RESTART',**bt2),sg.Text('--------', size=(5, 1), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , values = window.read()
        if button == "RESTART" :
            main_menu()

        if button == sg.WIN_CLOSED :
            break

    window.close()

main_menu()

