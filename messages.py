import pywhatkit

try:
    #pywhatkit.sendwhatmsg('+524443267363', 'Hola Mundo', 8, 35)
    pywhatkit.sendwhatmsg_instantly('+524443267363', 'Hola Mundo \n')
    print('Mensaje enviado')
except:
    print('Error al enviar'
    )

