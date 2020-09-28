import PySimpleGUI as sg

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
        button , value = window.read()
        if button == "START" :
            game()

        if button == "HOW TO PLAY ?" :
            sg.popup('Touch/Click the ball through the camera , When you tap it there will show your score with coundown timer :P')

        if button == sg.WIN_CLOSED :
            break

    window.close()

def game():
    layout =[

            [sg.Text('TIME : ', size=(15, 1), font=('Segoe UI', 18), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='time')],
            [sg.Text('SCORE : ', size=(15, 2), font=('Segoe UI', 18), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='score')],            
            [sg.Text('--------', size=(5, 10), font=('Segoe UI', 14), text_color='Black')],
            [sg.Text('--------', size=(50, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('EXIT',**bt2)]
           
            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , value = window.read()
        if button == "EXIT" :
            score()

        if button == sg.WIN_CLOSED :
            break

    window.close()


def score() :
    
    layout =[

            [sg.Text('ONE-TOUCH', size=(23,2), justification='center', text_color='White', font=('Franklin Gothic Book', 40, 'bold'))],
            [sg.Text('--------', size=(8, 2), font=('Segoe UI', 14), text_color='Black'),sg.Text('SCORE : ', size=(10, 2), font=('Segoe UI', 25), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='White', key='score')],   
            [sg.Text('--------', size=(22, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('RESTART',**bt2),sg.Text('--------', size=(5, 1), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False)

    while True:
        button , value = window.read()
        if button == "RESTART" :
            main_menu()

        if button == sg.WIN_CLOSED :
            break

    window.close()

main_menu()

