import pyautogui
from time import sleep
def open_guest_win(chrome_pos, ico_pos, guest_pos,site):
    pyautogui.click(chrome_pos)
    pyautogui.click(ico_pos)
    pyautogui.click(guest_pos)
    pyautogui.typewrite(site)
    pyautogui.press('enter')
    sleep(2)
def login(login_click_pos, username, password, submit):
    pyautogui.click(login_click_x,login_click_y)#clicks the login button from the homepage
    pyautogui.typewrite(username) #types the username
    pyautogui.press('tab')#presses tab to get the code to type in
    pyautogui.typewrite(password) #types the user password
    pyautogui.click(submit) # hits the button submit the login info

def open_tab(newtab_pos, second_site):
    pyautogui.click(newtab_pos)#opens the new tab
    pyautogui.typewrite(second_site) # enters the website name
    pyautogui.press('enter') #presses the enter button when the site domain is entered

