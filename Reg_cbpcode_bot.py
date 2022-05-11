#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update, context):
    """ Senda a message when the command / start is issued."""
    update.message.reply_text('HELLO')

def help(update, context):
    """Send a message when the command / help is issued."""
    update.message.reply_text ('help!')

#def echo(update, context):
    """Echo the user message."""
  #  update.message.reply_text(update.message.text)

def error(update, context):
    """log errors caused by updates."""
    logger.warning('Update"%s" caused error "%s"', update, context.error)

def pizza(update, context):
    if(update.message.text.upper().find("1001") > 0):
        update.message.reply_text("Adelante")

    if(update.message.text.upper().find("1002") > 0):
        update.message.reply_text("Identifiquese")

    if(update.message.text.upper().find("1003") > 0):
        update.message.reply_text("Cambie frecuencia")

    if(update.message.text.upper().find("1004") > 0):
        update.message.reply_text("Llamar por telefono")

    if(update.message.text.upper().find("1005") > 0):
        update.message.reply_text("Comprendido")

    if(update.message.text.upper().find("1006") > 0):
        update.message.reply_text("Afirmativo")
    
    if(update.message.text.upper().find("1007") > 0):
        update.message.reply_text("Se dirige a")

    if(update.message.text.upper().find("1008") > 0):
        update.message.reply_text("Repita mensaje")

    if(update.message.text.upper().find("1009") > 0):
        update.message.reply_text("Negativo")

    if(update.message.text.upper().find("1010") > 0):
        update.message.reply_text("Comunicacion de: / con:")
    
    if(update.message.text.upper().find("1011") > 0):
        update.message.reply_text("Comanda la unidad")

    if(update.message.text.upper().find("1012") > 0):
        update.message.reply_text("Permanezca en escucha")

    if(update.message.text.upper().find("1013") > 0):
        update.message.reply_text("Derrotero")

    if(update.message.text.upper().find("1014") > 0):
        update.message.reply_text("Consultar / Se consulta")

    if(update.message.text.upper().find("1015") > 0):
        update.message.reply_text("Efectivos")

    if(update.message.text.upper().find("1016") > 0):
        update.message.reply_text("Indique proporciones / Codifique")

    if(update.message.text.upper().find("1017") > 0):
        update.message.reply_text("Informe novedades")

    if(update.message.text.upper().find("1018") > 0):
        update.message.reply_text("Direccion")
    
    if(update.message.text.upper().find("1019") > 0):
        update.message.reply_text("Ubicacion")

    if(update.message.text.upper().find("1020") > 0):
        update.message.reply_text("En el lugar")

    if(update.message.text.upper().find("1021") > 0):
        update.message.reply_text("Linea privada")

    if(update.message.text.upper().find("1022") > 0):
        update.message.reply_text("En sintonia")
    
    if(update.message.text.upper().find("1023") > 0):
        update.message.reply_text("Se retira del lugar")

    if(update.message.text.upper().find("1024") > 0):
        update.message.reply_text("Urgente")

    if(update.message.text.upper().find("1025") > 0):
        update.message.reply_text("Emergencia confirmada")

    if(update.message.text.upper().find("1026") > 0):
        update.message.reply_text("En servicio")
    
    if(update.message.text.upper().find("1027") > 0):
        update.message.reply_text("Disponible")

    if(update.message.text.upper().find("1028") > 0):
        update.message.reply_text("Emergencia cancelada")

    if(update.message.text.upper().find("1029") > 0):
        update.message.reply_text("Mantenerse alerta")

    if(update.message.text.upper().find("1030") > 0):
        update.message.reply_text("Ingresa a su cuartel")
    
    if(update.message.text.upper().find("1031") > 0):
        update.message.reply_text("Transporte / traslado")

    if(update.message.text.upper().find("1032") > 0):
        update.message.reply_text("Emergencia en Progreso")

    if(update.message.text.upper().find("1033") > 0):
        update.message.reply_text("Emergencia dominada")

    if(update.message.text.upper().find("1034") > 0):
        update.message.reply_text("Tomar precauciones")
    
    if(update.message.text.upper().find("1035") > 0):
        update.message.reply_text("Requiere Policia")

    if(update.message.text.upper().find("1036") > 0):
        update.message.reply_text("Fuera de sintonia")

    if(update.message.text.upper().find("1037") > 0):
        update.message.reply_text("Requiere empresa electrica")

    if(update.message.text.upper().find("1038") > 0):
        update.message.reply_text("Abastecimiento de: (indique)")
    
    if(update.message.text.upper().find("1039") > 0):
        update.message.reply_text("Fuera de servicio")

    if(update.message.text.upper().find("1040") > 0):
        update.message.reply_text("Espere ordenes superiores")

    if(update.message.text.upper().find("1041") > 0):
        update.message.reply_text("Herido")

    if(update.message.text.upper().find("1042") > 0):
        update.message.reply_text("Muerto")
    
    if(update.message.text.upper().find("1043") > 0):
        update.message.reply_text("Herido efectivo FF.AA / FF.PP")

    if(update.message.text.upper().find("1044") > 0):
        update.message.reply_text("Paramedico")

    if(update.message.text.upper().find("1045") > 0):
        update.message.reply_text("Medico")

    if(update.message.text.upper().find("1046") > 0):
        update.message.reply_text("Enfermo")
    
    if(update.message.text.upper().find("1047") > 0):
        update.message.reply_text("No interrumpir")

    if(update.message.text.upper().find("1048") > 0):
        update.message.reply_text("Piloto rentado")

    if(update.message.text.upper().find("1049") > 0):
        update.message.reply_text("Bombero maquinista")

    if(update.message.text.upper().find("1050") > 0):
        update.message.reply_text("En estado de alerta")
    
    if(update.message.text.upper().find("1051") > 0):
        update.message.reply_text("Parturienta")

    if(update.message.text.upper().find("1052") > 0):
        update.message.reply_text("Toque sirena")

    if(update.message.text.upper().find("1053") > 0):
        update.message.reply_text("Regrese a su cuartel")

    if(update.message.text.upper().find("1054") > 0):
        update.message.reply_text("Prosiga la marcha")
    
    if(update.message.text.upper().find("1055") > 0):
        update.message.reply_text("Requiere de empresa de Agua")

    if(update.message.text.upper().find("1056") > 0):
        update.message.reply_text("Dejar sin efecto")

    if(update.message.text.upper().find("1057") > 0):
        update.message.reply_text("Utilize claves")

    if(update.message.text.upper().find("1058") > 0):
        update.message.reply_text("Fin de estado de alerta")
    
    if(update.message.text.upper().find("1059") > 0):
        update.message.reply_text("Guardia nocturna")

    if(update.message.text.upper().find("1060") > 0):
        update.message.reply_text("Identificacion de la emergenia")

    """if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")
    
    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")
    
    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("x")

    if(update.message.text.upper().find("100") > 0):
        update.message.reply_text("que novedades")"""







def main():
    """start the bot"""
    # create updater
    # make sure the setr
    # post version
    updater = Updater("5302231449:AAF9AOKjDGTmlWR-6eLu9D8agkEmDfdoEJg", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on non command i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, pizza))

    # log all errors
    dp.add_error_handler(error)

    # start the bot
    updater.start_polling()

    # Run bot until you press ctrl-c or the process receives SIGNT,
    #
    #
    updater.idle()


if __name__ == "__main__":
    main()