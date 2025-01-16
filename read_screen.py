

from wordle_words import words
from prosess_result import Game




from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



game = Game(words)


# create webdriver object 
driver = webdriver.Chrome()
url="https://www.nytimes.com/games/wordle/index.html"
driver.get(url)
time.sleep(5)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "fides-reject-all-button")))
time.sleep(0.4)
driver.find_element(By.CLASS_NAME,'fides-reject-all-button').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "purr-blocker-card__button").click()
time.sleep(1)
btn=driver.find_elements(By.CLASS_NAME, "Welcome-module_button__ZG0Zh")[2].click()
time.sleep(10)
driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb").click()
element=driver.find_element(By.CLASS_NAME, "Board-module_boardContainer__TBHNL")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(1)

guess=game.find_best_word(game.count_letters())
body = driver.find_element(By.TAG_NAME, "body")

for t in range(5):
    body.send_keys(guess) 
    body.send_keys(Keys.ENTER) 
    time.sleep(3)
    row=driver.find_elements(By.CLASS_NAME,"Tile-module_tile__UWEHN")
    result=[]
    for i in range(t*5,5*(t+1)):
        result.append(row[i].accessible_name.split(",")[2])
    if result==[" correct"," correct"," correct"," correct"," correct" ]:
        print("YOU WON !!!!!!!!!!!!!!!!!!!!")
        break
    game.prosess_result_from_screen(result,guess)
    game.make_new_word_list()
    guess=game.find_best_word(game.count_letters())




time.sleep(1000000)

























