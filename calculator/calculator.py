#Student ID : 6201012620139
#Name : Natthamon Bunnithi
#ref1 : https://github.com/israel-dryer/PyDataMath-II
#ref2 : http://myblogmysoftware.blogspot.com/2018/09/pysimplegui-based-basic-calculator.html
#------------------------Calculator with  PySimpleGUI-------------------------------#

import PySimpleGUI as sg 
#-------------------------Interface Calculator-----------------------------------#
# color in hex
Black = '#000000'
Blue = '#05426c'
DarkGreen = '#99c5c0'
LightGreen = '#a2eee3'

#set backgroung color
sg.theme('BrightColors') 

# display caption, buttons size 
form = sg.FlexForm('CALCULATOR', default_button_element_size=(8, 4), auto_size_buttons=False, grab_anywhere=True)

#create gui interface with input,button,color,size
layout = [
            [sg.Text('INPUT YOUR MATH :)', size=(23,1), justification='left', text_color='Black', font=('Franklin Gothic Book', 14, 'bold'))],
            [sg.Input(size=(45,1), do_not_clear=True, justification='right', key='input')],
            [sg.Text('Ans :', size=(15, 1), font=('Segoe UI', 14), text_color='Blue')],[sg.Text('', size=(14, 1), font=('Segoe UI', 18), text_color='Black', key='out')],
            [sg.ReadFormButton('CE',button_color=(Black,DarkGreen)), sg.ReadFormButton('DEL',button_color=(Black,DarkGreen)),sg.ReadFormButton('(',button_color=(Black,DarkGreen)), sg.ReadFormButton(')',button_color=(Black,DarkGreen))], 
            [sg.ReadFormButton('7',button_color=(Black,LightGreen)), sg.ReadFormButton('8',button_color=(Black,LightGreen)), sg.ReadFormButton('9',button_color=(Black,LightGreen)), sg.ReadFormButton('/',button_color=(Black,DarkGreen))],
            [sg.ReadFormButton('4',button_color=(Black,LightGreen)), sg.ReadFormButton('5',button_color=(Black,LightGreen)), sg.ReadFormButton('6',button_color=(Black,LightGreen)), sg.ReadFormButton('*',button_color=(Black,DarkGreen))],
            [sg.ReadFormButton('1',button_color=(Black,LightGreen)), sg.ReadFormButton('2',button_color=(Black,LightGreen)), sg.ReadFormButton('3',button_color=(Black,LightGreen)), sg.ReadFormButton('-',button_color=(Black,DarkGreen))],
            [sg.ReadFormButton('.',button_color=(Black,DarkGreen)),sg.ReadFormButton('0',button_color=(Black,LightGreen)), sg.ReadFormButton('SUBMIT',button_color=(Black,DarkGreen)), sg.ReadFormButton('+',button_color=(Black,DarkGreen))],
        ]

form.Layout(layout)
# for input
keys_input = '' 

#---------------------------Running Program-----------------------------------#
running = True
while running:
    button, values = form.Read() # read the form 
    try:

        if button == 'SUBMIT':  
            keys_input = values['input']  
            sum = eval(keys_input)  
            form.FindElement('out').Update(sum)  

    except ZeroDivisionError:  # if /0 will error
     form.FindElement('out').Update('Error') 

    except SyntaxError:  #if syntax error
     form.FindElement('out').Update('Error')  

    if button == None: # if the X button clicked, just exit  
        break  

    if button == 'CE': # clear all element 
        keys_input = ''  

    elif button == 'DEL':  # delete the last number or operator 
        keys_input = values['input']  
        keys_input = keys_input[:-1]  

    elif button in '()1234567890./*-+' :  # if is operator or operand
        keys_input = values['input']   
        keys_input += button 

    # change the form to reflect current key string 
    form.FindElement('input').Update(keys_input)
