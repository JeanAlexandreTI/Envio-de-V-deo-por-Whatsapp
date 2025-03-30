# %%

from time import sleep
import playsound as play
import pyautogui as pygui
import selenium
from selenium import webdriver

# %%
contatos = {
    'jao' : ['jao', 'https://www.youtube.com/watch?v=dYrP2DKB02A']
}

# %%
# Saber posicao do cursor do mouse
pygui.position()

# %%
pygui.moveTo(555, 767) 
sleep(1)

pygui.click(555, 741) #Apertar o botao de pesquisa
pygui.write('whatsapp') #Escreve whatsapp
pygui.press('enter') #Abre whatsapp com enter
sleep(4)

# Abrir conversa com meu mano Jao
pygui.write(contatos['jao'][0])
pygui.press('enter')
pygui.press('down')
pygui.press('enter')

# Enviar arquivo de audio
sleep(2)
pygui.write(contatos['jao'][2])

pygui.press('enter')

