#####################################################
#   Baixar arquivo com CadPro ativos no PR          #
#####################################################

#Bibliotecas
import pyautogui
import pymsgbox
import time

#pymsgbox.alert(text='FAVOR AGUARDAR PROCEDIMENTO AUTOMÁTICO!', title='NÃO MEXER', button='OK')
#time.sleep(1.5)
#pyautogui.press('esc')




pyautogui.hotkey('alt', 'tab')
time.sleep(1)

#1 - Abre o navegador (Chrome)
#pyautogui.hotkey('winleft')
#pyautogui.write('chome', interval=0.50)
#pyautogui.press('enter')



#2 - Abre o site da fazenda salvo nos favoritos
#pyautogui.hotkey('ctrl', 't')
time.sleep(1)
#pyautogui.write('http://processos.fazenda.pr.gov.br/arquivos/pubcadpro', interval=0.10)
#pyautogui.press('enter')            
time.sleep(1)

imgExtrair = pyautogui.locateCenterOnScreen('C:\\xampp\\htdocs\\portfolio\\_base\\_extrair.png', confidence=0.9)
pyautogui.click(imgExtrair)
#pyautogui.click(button='right')
exit()  

#abre gerenciador de downloads
pyautogui.hotkey('ctrl', 'j')
time.sleep(3)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('right') 
time.sleep(1)
pyautogui.press('enter') 
time.sleep(1)
pyautogui.hotkey('winleft', 'r')
time.sleep(1)
pyautogui.write('Downloads', interval=0.10)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('p')
time.sleep(1)
pyautogui.hotkey('ctrl', 'x')
time.sleep(1)
pyautogui.hotkey('winleft', 'r')
time.sleep(1)
pyautogui.write('C:\cadpro', interval=0.10)
time.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
imgExtrair = pyautogui.locateCenterOnScreen('C:\\xampp\\htdocs\\portfolio\\_base\\_extrair.png', confidence=0.7)
pyautogui.click(img8)
time.sleep(1)
pyautogui.press('down') 
time.sleep(1)
pyautogui.press('down') 
time.sleep(1)
pyautogui.press('down') 
time.sleep(1)
pyautogui.press('down') 
time.sleep(1)
pyautogui.press('down') 
time.sleep(1)
alert(text='Download do documento de CADPRO realizado com sucesso!', title='OBRIGADO', button='OK')


exit()     
       
#6 - Clica em "manter"
img6 = pyautogui.locateCenterOnScreen('C:\\xampp\\htdocs\\portfolio\\_base\\_mov6.png', confidence=0.7)
pyautogui.click(img6)
time.sleep(1)
  
#7 - Botão direito no arquivo 
img7 = pyautogui.locateCenterOnScreen('C:\\xampp\\htdocs\\portfolio\\_base\\_mov7.png', confidence=0.7)
pyautogui.click(button='right'(img7))
time.sleep(1)
    
#8 - Mostra na pasta
img8 = pyautogui.locateCenterOnScreen('C:\\xampp\\htdocs\\portfolio\\_base\\_mov8.png', confidence=0.7)
pyautogui.click(img8)
time.sleep(1)
    
#9 - Recorta arquivo
pyautogui.hotkey('ctrl', 'x')
time.sleep(1)
    
#10 - Navegar até a pasta C:\cadpro  (ctrl + e)
pyautogui.hotkey('winleft', 'r')
time.sleep(1)
pyautogui.write('C:\cadpro', interval=0.50)
time.sleep(1)
pyautogui.press('enter')

#11 - Colar arquivo
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)


alert(text='Download do documento de CADPRO realizado com sucesso!', title='OBRIGADO', button='OK')

