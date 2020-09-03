import discord, asyncio
import time
import win32api
from os import system
from datetime import datetime

system("title Feito por Shatra#0147!")
win32api.MessageBox(0, 'Feito por Shatra#0147!', 'Créditos:')
d1 = datetime.now()                       # <- Pegando informações de horário;
potato = d1.strftime("%H:%M:%S-%d/%m/%Y") # <- Formatando em horas/minutos/segundos - dia/mês/ano
client = discord.Client()                 # <- Criando o Client;
token = "" # <- O token da sua conta;
print(""" 
       ...                                      s                             
   .x888888hx    :   .uef^"                    :8                             
  d88888888888hxx  :d88E                      .88       .u    .               
 8" ... `"*8888%`  `888E             u       :888ooo  .d88B :@8c        u     
!  "   ` .xnxx.     888E .z8k     us888u.  -*8888888 ="8888f8888r    us888u.  
X X   .H8888888%:   888E~?888L .@88 "8888"   8888      4888>'88"  .@88 "8888" 
X 'hn8888888*"   >  888E  888E 9888  9888    8888      4888> '    9888  9888  
X: `*88888%`     !  888E  888E 9888  9888    8888      4888>      9888  9888  
'8h.. ``     ..x8>  888E  888E 9888  9888   .8888Lu=  .d888L .+   9888  9888  
 `88888888888888f   888E  888E 9888  9888   ^%888*    ^"8888*"    9888  9888  
  '%8888888888*"   m888N= 888> "888*""888"    'Y"        "Y"      "888*""888" 
     ^"****""`      `Y"   888   ^Y"   ^Y'                          ^Y"   ^Y'  
                         J88"                                                 
                         @%                                                   
                       :"                                                     
""")
print("Código feito por: Shatra#0147")

# <-> Receber o evento MESSAGE;
@client.event
async def on_message(message):
   try:
        canal = message.channel
        server = message.guild
		
		# <-> POLLUX
        if message.author.id == 271394014358405121: # -> Caso o autor da mensagem possua o ID da POLLUX;
           if message.content.startswith(str("Entries for this Box:")): # -> Caso o conteudo da mensagem for o sorteio da POLLUX;
               for i in range(0,1):  # -> Aqui temos um "timer" pra dar um "delay" na velocidade da mensagem;
                 time.sleep(1.3)     # -> Aplica o "delay" | Quanto maior a quantidade, mais lento é pra enviar;
                 await canal.send("pick"), print(f"[?] Participando do pick: [{canal.name}] - [{server.name}] / {potato}")

		# <-> Caso ganhe o sorteio		
        if message.author.id == 271394014358405121: # -> Caso o autor da mensagem possua o ID da POLLUX;
          if str(message.mentions).find(f"{client.user.id}") != -1: # -> Procuramos a sua mensão na mensagem da POLLUX, caso o "find" não seja -1, ele prossegue;
           print(f"[$] Pick ganho no chat: [{canal.name}] - [{server.name}] / {potato}")
           
		# <-> DIANA
        if message.author.id == 736973289439887442: # -> Caso o autor da mensagem possua o ID da DIANA;
           if message.content.startswith(str("A Transportadora de valores mandou um carro forte com")):
               for i in range(0,1): # <-> Aqui temos um "timer" pra dar um "delay" na velocidade da mensagem;
                 time.sleep(1.3)    # <-> Aplica o "delay" | Quanto maior a quantidade, mais lento é pra enviar;
                 await canal.send("roubar"), print(f"[?] Participando do roubo: [{canal.name}] - [{server.name}] / {potato}")

		# <-> Caso ganhe o sorteio		 
        if message.author.id == 736973289439887442: # -> Caso o autor da mensagem possua o ID da DIANA;
          if str(message.mentions).find(f"{client.user.id}") != -1: # -> Procuramos a sua mensão na mensagem da DIANA, caso o "find" não seja -1, ele prossegue;
           print(f"[$] Roubo ganho no chat: [{canal.name}] - [{server.name}] / {potato}")     
   except:
               pass

client.run(token, bot=False) # Faz o login utilizando sua TOKEN.
