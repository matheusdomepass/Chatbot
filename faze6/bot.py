# =======================================================================================
# importação das bibliotecas
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.trainers import ListTrainer

# =======================================================================================    
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  
# =======================================================================================   
# instânciando um objeto ChatBot
bot = ChatBot('Tonks', read_only=True, 
              response_selection_method=get_most_frequent_response,     
              storage_adapter="chatterbot.storage.SQLStorageAdapter",
              database_uri='sqlite:///database.sqlite3'
              )

# =======================================================================================   
# treinando o bot a partir de um arquivo texto
treinador = ListTrainer(bot)

conversa = open("conversa.txt", encoding="utf-8", errors="ignore").read().split("\n") 
treinador.train(conversa)
conversa1 = open("conversa1.txt", encoding="utf-8", errors="ignore").read().split("\n")
treinador.train(conversa1)
conversa2 = open("conversa2.txt", encoding="utf-8", errors="ignore").read().split("\n")
treinador.train(conversa2)
conversa3 = open("conversa3.txt", encoding="utf-8", errors="ignore").read().split("\n")
treinador.train(conversa3)
conversa4 = open("conversa4.txt", encoding="utf-8", errors="ignore").read().split("\n")
treinador.train(conversa4)
conversa5 = open("conversa5.txt", encoding="utf-8", errors="ignore").read().split("\n")
treinador.train(conversa5)
conversa6 = open("conversa6.txt", encoding="utf-8", errors="ignore").read().split("\n")
treinador.train(conversa6)
conversa7 = open("conversa7.txt", encoding="utf-8", errors="ignore").read().split("\n") 
treinador.train(conversa7)
conversa8 = open("conversa8.txt", encoding="utf-8", errors="ignore").read().split("\n") 
treinador.train(conversa8)
conversa9 = open("conversa9.txt", encoding="utf-8", errors="ignore").read().split("\n") 
treinador.train(conversa9)
conversa10 = open("conversa10.txt", encoding="utf-8", errors="ignore").read().split("\n") 
treinador.train(conversa10)

# =======================================================================================  
# função que retorna a página html
@app.route("/")
def home():
    return render_template("index.html")
# =======================================================================================
# função que pega a mensagem do usuário e devolve a resposta do bot
@app.route("/get")
def get_bot_response():
    while True:
        try:
            pergunta = userText = request.args.get('msg')        
            resposta = bot.get_response(pergunta)
            if float(resposta.confidence) > 0.5:
                return str(resposta)
            else:
                return str(' Desculpe . . . Ainda não sei responder esta pergunta.') 
                #return str(' Entendo que esteja passando por uma situação difícil, infelizmente sou apenas um chatbot. . . Eu recomendo buscar ajuda profissional. Você pode entrar no site: " zenklub.com.br ". Nele você terá ajuda psicológica gratuitamente. E, causo esteja procurando por mais informações, entre no site: " centralpsicologia.com.br/blog " . Nele você encontra vários artigos.')
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
        
# =======================================================================================
# inicia o programa
if __name__ == "__main__":
    app.run()
# =======================================================================================            