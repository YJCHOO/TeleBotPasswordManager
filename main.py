from telegram.ext import Updater, CommandHandler
from password_generator import PasswordGenerator

token = 'token'

def hello(update, context):
    update.message.reply_text('Hi, {}.'.format(update.message.from_user.first_name))

def generatePassword(update, context):
    password = PasswordGenerator().generatePassword()
    update.message.reply_text(password)

updater = Updater(token, use_context = True)

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('generate_password', generatePassword))

updater.start_polling()
updater.idle()
