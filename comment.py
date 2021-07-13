from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def instagram_comment_bot(username, password, post_link):

   number_comments = input("Escreva o número de comentários que você quer fazer:\n")
   comments = []
   for i in range(int(number_comments)):
      comments.append(input("Escreva um comentário:\n"))
      
   number_combinations = input("Caso você queira que em um mesmo comentário haja uma combinação dos textos que você escreveu anteriormente, digite o número de combinações (digite 0 para caso queira um comentário único):\n")

   print("Avisos:")
   sleep(2)
   print("Esse programa busca fazer aproximadamente 100 comentários na mesma postagem sem que o instagram o derrube ou derrube sua conta.")
   sleep(4)
   print("Recomenda-se que se faça o uso dele no máximo 3 vezes em um dia.")
   sleep(4)
   print("Mesmo assim, o Instagram pode emitir um alerta que sua conta foi usada como spam (ou algo do tipo) e há a possibilidade que sua conta seja suspensa por um curto período.")
   sleep(4)
   print("Ou seja, use com moderação.\n")
   sleep(4)
   print("Por fim, sua conta deve estar com a verificação em duas etapas desativada.")
   sleep(4)
   print("Lembre-se de desativá-la antes de confirmar confirmar a sua ação.")
   sleep(4)
   print("Quando o programa terminar, lembre-se de ativar a verificação em duas etapas para maior segurança de sua conta.")
   sleep(4)

   confirmacao = input("Ativar o bot de comentários (use 1 para sim e 0 para não):\n")

   if confirmacao == 0:
      return

   binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

   browser  = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')
   browser.implicitly_wait(5)

   browser .get('https://www.instagram.com/')
   
   username_input = browser.find_element_by_css_selector("input[name='username']")
   password_input = browser.find_element_by_css_selector("input[name='password']")

   username_input.send_keys(username)
   password_input.send_keys(password)

   login_button = browser.find_element_by_xpath("//button[@type='submit']")
   login_button.click()

   sleep(10)

   for i in range(random.randint(97,103)):
      if random.randint(0,10) == 5:
         sleep(60)
      browser .get(post_link)


      sleep(random.randint(5, 10))
      commentArea = browser.find_element_by_class_name('Ypffh')
      commentArea.click()
      commentArea = browser.find_element_by_class_name('Ypffh')
      index = random.randint(3,30)%len(comments)
      comment = comments[index]
      if i != 0:
         for i in range(1,int(number_combinations)):
            comment = comment + " " +comments[(index+i)%len(comments)]
      commentArea.send_keys(comment)
      sleep(1)
      # commentArea.send_keys(Keys.ENTER)
      sleep(1)
      # commentArea.send_keys(Keys.ENTER)
      
      browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]").click()
      print(i+1)
      sleep(random.randint(7, 10))

   return

def menu():
   print("Bem-vindo!")
   sleep(2)
   print("Antes de começar, verfique se você seguiu todos os passos que estão no repositório do GitHub.")
   print("Seguiu? Vamos lá então.")
   print("Vamos te autenticar no Instagram. Para isso, vamos precisar seu username e sua senha.")
   print("Não se preocupe, suas informações não ficam salvas.")
   username = input("Digite seu username do instagram:\n")
   password = input("Digite sua senha:\n")
   print("Agora, vamos para a configuração do bot.")
   sleep(3)
   print("Então quer dizer que você quer ganhar um sorteio?")
   sleep(3)
   post_link = input("Digite o link da postagem do Instagram (obtenha-o acessando o Instagram Web):\n")
   instagram_comment_bot(username,password,post_link)
   print("Processo finalizado. Boa sorte no seu sorteio! :)")

menu()




