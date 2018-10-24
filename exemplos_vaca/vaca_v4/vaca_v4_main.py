from vaca_v4 import *

''' ================= '''
''' Main (Big Bang):
'''



'''
Jogo -> Jogo
inicie o mundo com JOGO_INICIAL
'''
def main(inic):
    big_bang(inic,  # Jogo
             tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_tudo,  # Jogo -> Jogo
             desenhar=desenha_jogo,  # Jogo -> Imagem
             quando_tecla=trata_tecla_jogo,  # Vaca Tecla -> Vaca
             quando_solta_tecla=trata_solta_jogo,  # Jogo Tecla -> Jogo
             modo_debug=True
             )



''' Vaca -> Vaca '''
''' inicie o mundo com VACA_INICIAL '''
def main_vaca(inic):
    big_bang(inic,   # Vaca
             tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_vaca,  # Vaca -> Vaca
             desenhar=desenha_vaca,   # Vaca -> Imagem
             quando_tecla=trata_tecla_vaca, # Vaca Tecla -> Vaca
             modo_debug=True
             )

main(JOGO_INICIAL)