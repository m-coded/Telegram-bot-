import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5357278018:AAHOpt5yq0ZvcN0xphM2EjH7XW8_nRUOPhQ'
    bot_chatID = '5302111878'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def correct():
    telegram_bot_sendtext()

a = 33
b = 200
if b > a:

   telegram_bot_sendtext("b is greater than a")


 
 
 

    

 
 