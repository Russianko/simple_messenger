from flask import Flask, request, render_template

app = Flask(__name__)

# как толко ползовательь окрывает страницу "/" выполняется ниже функция
# а ее резулат отображается в браузере
@app.route('/')
def main_page():
    return 'Hello! Welcome to messenger'


from datetime import datetime

# all messages are reading from this list
all_messages = []

def add_message(sender, text):
    # create new message (dict) and add it to list
    today = datetime.today()
    new_message = {
        "name" : sender,
        "text" : text,
        "time" : today.strftime('%d/%m/%Y %H:%M:%S') # !!!  ДЗ  1!!!!подставить текущее время часы минуты
    }
    all_messages.append(new_message)



add_message('Russianko', 'Hello world!')
add_message('Алюня', 'Hello!')
add_message('Russianko', 'Are you world?')


@app.route('/get_messages')
def get_messages():
    return {"messages": all_messages} # сообщения отобразятся в формате JSon

# Http-GET запрос
# /send_message?name=Alyunya&text=Hello
@app.route("/send_message")
def send_message():
    name = request.args.get("name")
    text = request.args.get("text")
    add_message(name, text)
    # ДЗ добавить проверку имени  текста  выдавать ошибку
    return "Message Sent"


@app.route("/chat")
def chat_page():
    return render_template("chat.html")



app.run(debug=True)

