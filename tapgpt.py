import wolframalpha
import wikipedia
client = wolframalpha.Client("R82GJU-PPXGG6PAHH")

import PySimpleGUI as sg                     
sg.theme('DarkPurple1')

layout = [  [sg.Text("How can I help?")],     
            [sg.Input()],
            [sg.Button('Ok'),sg.Button('Cancel'),sg.Button('wolframealpha'),sg.Button('Wiki'),sg.Button('Chatgpt')]] 


window = sg.Window('brajMohan', layout)      



while True:
    event,values = window.read()
    
    try:
        res =client.query(values[0])  
        wolfram_res = next(res.results).text
        sg.Popup(wolfram_res)    
    except:
        wiki_res=wikipedia.summary(values[0],sentences=1)
        sg.Popup(wiki_res)
    if event =='wolframealpha':
        res =client.query(values[0])  
        wolfram_res = next(res.results).text
        sg.Popup(wolfram_res)    
    if event=='Wiki':
        wiki_res=wikipedia.summary(values[0],sentences=1)
        sg.Popup(wiki_res) 
    if event in (None,'Cancel'):
        break  
    print(values[0],'is')       
window.close()                                 