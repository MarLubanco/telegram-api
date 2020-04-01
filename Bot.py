# -*- coding: utf-8 -*-
import telepot
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/send', methods=['POST'])
def sendMessage():
    mensagem = str(request.json["mensagem"])
    document = str(request.json["documento"])
    bot = telepot.Bot("1138404020:AAEI3k-kO5gSFr9YAXd4C3SkeQVeuY8KVZk")
    botCreate = bot.getMe()
    contatos = bot.getUpdates()
    idsContatos = []
    for contato in contatos:
        idsContatos.append(contato['message']['from']['id'])
    idsContatos = list(set(idsContatos))
    for id in idsContatos:
        bot.sendMessage(id, mensagem)
        if(document) :
            bot.sendDocument(id, (open(document, "rb")), 'meu-amor')
        print("Mensagem enviada com sucesso, id: ", id)
    return 'Todo...'

@app.route('/index',  methods=['GET','POST'])
def formexample():
    if request.method == 'POST':
        mensagem = str(request.form.get("mensagem"))
        document = str(request.form.get("documento"))
        bot = telepot.Bot("1138404020:AAEI3k-kO5gSFr9YAXd4C3SkeQVeuY8KVZk")
        botCreate = bot.getMe()
        contatos = bot.getUpdates()
        idsContatos = []
        for contato in contatos:
            idsContatos.append(contato['message']['from']['id'])
        idsContatos = list(set(idsContatos))
        for id in idsContatos:
            bot.sendMessage(id, mensagem)
            if (document):
                bot.sendDocument(id, open(document, "rb"), 'meu-amor')
            print("Mensagem enviada com sucesso, id: ", id)

    return '''
       <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        </head>
         <body class="container">
            <div class="jumbotron" >
                <p class="h1 text-center">Menssagem em Massa</p>
                <p class="h2 text-center">Telegram</p>
                 <div class="row text-center">
                   <div class="col-md-4"></div>
                   <div class="text-center col-md-4">
                        <form method="POST">
                            Mensagem: <input class="form-control" type="text" name="mensagem"><br>
                            Documento: <input class="form-control" type="file" name="documento"><br>
                            <input class="btn btn-success" type="submit" value="Enviar Mensagem"><br>
                        </form>''
                  </div>
              </div>
           </div>
        </body>            
        </html>'''


    # return ("""
    #        <html>
    #    <head>
    #        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    #        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    #        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    #    </head>
    #    <script>
    #        var casosMundiais = []
    #    getAllCases()
    #        function getAllCases() {
    #            var valor = document.getElementById("mensagem").value
    #            var arquivo = document.getElementById("arquivo").value
    #            var request = new XMLHttpRequest()
    #
    #            const url = "http://localhost:8080/send";
    #            fetch(url, {
    #                method : "POST",
    #                body : {
    #                     mensagem : valor,
    #                     documento: arquivo
    #                }
    #            }).then(
    #                response => response.text() // .json(), etc.
    #            ).then(
    #                html => console.log(html)
    #            );
    #
    #
    #        }
    #
    #    </script>
    #    <body class="container">
    #        <div class="jumbotron" >
    #            <p class="h1 text-center">Menssagem em Massa</p>
    #            <p class="h2 text-center">Telegram</p>
    #            <div class="row text-center">
    #                <div class="col-md-4"></div>
    #                <div class="text-center col-md-4">
    #                        <input class="form-control" id="mensagem" placeholder="Mensagem a ser enviada..." type="text">
    #                        <hr>
    #                        <input id="arquivo" class="form-control" type="file">
    #                        <button class="btn btn-info center" onclick="getAllCases()" >Enviar</button>
    #                </div>
    #            </div>
    #        </div>
    #
    #    </body>
    #
    #    </html>
    #        """)

@app.route('/json-example')
def jsonexample():
    return 'Todo...'

if __name__ == '__main__':
    app.run(host= 'localhost', debug=True, port=8080) #run app in debug mode on port 5000



# bot = telepot.Bot("1138404020:AAEI3k-kO5gSFr9YAXd4C3SkeQVeuY8KVZk")
# botCreate = bot.getMe()
# contatos = bot.getUpdates()
# idsContatos = []
# for contato in contatos:
#     idsContatos.append(contato['message']['from']['id'])
# mensagem = """
# Olá, bom dia cliente, nós estamos com uma promoção INCRIVEL,
# MAS SOMENTE ESSA SEMANA
#
# 50% DE DESCONTO
#
# Aproveite
#
# Nos responda e ganhe seu produto
# """
# document =  "" #"/home/thome/Área de Trabalho/debora.jpeg"
# idsContatos = list(set(idsContatos))
# for id in idsContatos:
#     bot.sendMessage(id, mensagem)
#     if(document) :
#         bot.sendDocument(id, (open(document, "rb")), 'meu-amor')
#     print("Mensagem enviada com sucesso, id: ", id)