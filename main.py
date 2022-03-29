# -*- coding: utf-8 -*-
"""FirstBot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UxNDMYemik4Cc3Lkt_GcxGHoOFBAopq2
"""

import os

from flask import Flask, request
from telebot import types

import telebot

bot = telebot.TeleBot('5193517482:AAGGvbbnKU9_RNHATEKH3Ocp-xvA7Bi_tIA')
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
  kb = types.ReplyKeyboardMarkup()
  kb.add("QR")
  kb.add("Картинка")

  bot.send_message(message.chat.id, "Здравствуйте, что бы вы хотели сделать?", reply_markup=kb)

@server.route("/")
def webhook():
    bot.remove_webhook()
   
    bot.set_webhook(url='https://botik322.herokuapp.com/' + '5193517482:AAGGvbbnKU9_RNHATEKH3Ocp-xvA7Bi_tIA')
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
