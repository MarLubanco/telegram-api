# -*- coding: utf-8 -*-
import telepot

bot = telepot.Bot("1138404020:AAEI3k-kO5gSFr9YAXd4C3SkeQVeuY8KVZk")
botCreate = bot.getMe()
contatos = bot.getUpdates()
idsContatos = []
for contato in contatos:
    idsContatos.append(contato['message']['from']['id'])
mensagem = """
Olá, bom dia cliente, nós estamos com uma promoção INCRIVEL, 
MAS SOMENTE ESSA SEMANA

50% DE DESCONTO

Aproveite

Nos responda e ganhe seu produto
"""
document =  "" #"/home/thome/Área de Trabalho/debora.jpeg"
idsContatos = list(set(idsContatos))
for id in idsContatos:
    bot.sendMessage(id, mensagem)
    if(document) :
        bot.sendDocument(id, (open(document, "rb")), 'meu-amor')
    print("Mensagem enviada com sucesso, id: ", id)