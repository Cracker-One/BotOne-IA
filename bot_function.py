import datetime
def response_bot(rsp):
    if('salut' in rsp): print('Bot : '+str('salut, comment vas-tu ?'))
    if('quel âge as-tu' in rsp): print('Bot : '+str("J'ai 0 ans"))
    if('quel est ton nom' in rsp): print('Bot : '+str("Mon nom est BotOne"))
    if('où vis-tu' in rsp): print('Bot : '+str("Je vis dans ton pc"))
