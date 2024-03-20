#!/usr/bin/python3.5

# - - - - - - - - - - - - - - - - - - - - - - - - -
# Aplicação para Criptografia AES
# Autores: Leonardo Migot e Maico A. C. Souza
# Data: Out/2016
# 
# 	Capacidades:
# 	Modos: EBC e CBC.
# 	Chaves: 128, 192 e 256 bits.
#	Encripta e decriptar.
#	Criar vetores de inicialização (128 bits)
#   Encriptar arquivos de tamanhos variados.
#
# - - - - - - - - - - - - - - - - - - - - - - - - -

# # # # # # # # # # # # 

# - - - Imports - - - #

# # # # # # # # # # # #

from Crypto.Cipher import AES
from Crypto import Random
import random
import easygui
from struct import *
import binascii
import base64
import os


# # # # # # # # # #

# - - - GUI - - - #

# # # # # # # # # #

def start():
    return easygui.buttonbox('O que você deseja fazer?', '', ['Encriptar', 'Decriptar', 'Sair'])

def mode():
    return easygui.buttonbox('Qual modo de operação?', '', ['ECB', 'CBC'])
 
def k_or_p():
    return easygui.buttonbox('O que você deseja utilizar?', '', ['Nova Chave', 'Chave Existente', 'Senha'])

def IV_exist():
    return easygui.buttonbox('Vetor de inicialização?', '', ['Novo IV', 'IV Existente'])

def k_or_p2():
    return easygui.buttonbox('O que você deseja utilizar?', '', ['Chave Existente', 'Senha'])

def key_size():	
    return easygui.buttonbox('Qual o tamanho da chave?', '', ['128', '192', '256'])

def key_open():
    easygui.msgbox('Escolha a chave...')
    return easygui.fileopenbox('Chave...')

def key_save():
	easygui.msgbox('Salvar a chave...')
	return easygui.filesavebox('Chave...')

def IV_save():
	easygui.msgbox('Salvar o IV...')
	return easygui.filesavebox('IV...')

def password():
    return easygui.passwordbox('Digite a senha (16 bytes / 16 caracteres):')

def file_open():
    easygui.msgbox('Escolha um arquivo...')
    return easygui.fileopenbox('Arquivo...')

def IV_open():
    easygui.msgbox('Escolha o vetor de inicialização...')
    return easygui.fileopenbox('Arquivo...')

def file_save():
	easygui.msgbox('Salvar o arquivo após a operação...')
	return easygui.filesavebox('Arquivo...')
	
def warning():
	easygui.msgbox('Atenção! \nPara decriptar o arquivo selecionado futuramente, será necessario extrai-lo como um arquivo TAR. ')

# # # # # # # # # # # # 

# - - - Funções - - - #

# # # # # # # # # # # # 

def random_key(Vkey_size):
    Vkey_size = int(Vkey_size)
    Vkey_size = int(Vkey_size / 8)
    rndk = Random.new().read(Vkey_size)
    return rndk

def key_input(Vkey_open):
	file_k = open(Vkey_open,'r')
	key = file_k.readline()
	key = binascii.unhexlify(key)
	return key	

def key_output(Vkey_size, Vkey_save):
	key = random_key(Vkey_size)
	key = binascii.hexlify(key)
	key = key.decode('utf8')
	k_file = open(Vkey_save,'w+')	
	k_file.write(key)
	k_file.close()
	return key

def tkey_size(Vkey_open):
	size_k = open(Vkey_open,'r')
	key = file_k.readline()
	key = binascii.unhexlify(key)
	size_k.close()
	return len(key_size)

def tar_pad(plaintext, Vfile_open):

	div = len(plaintext) % 16

	if div != 0:
		os.system('tar cf pln.tar ' + Vfile_open)
		Vfile_open = 'pln.tar'
		warning()

	return Vfile_open


def AES_ECB(plaintext):

	var = AES.new(key, AES.MODE_ECB)

	if Vstart == 'Encriptar':

		ciphertext = var.encrypt(plaintext)
		ciphertext = binascii.hexlify(ciphertext)
		ciphertext = ciphertext.decode('utf8')

	elif Vstart == 'Decriptar':

		ciphertext = binascii.unhexlify(plaintext)
		ciphertext = var.decrypt(ciphertext)
		ciphertext = ciphertext.decode('utf8')		

	ciphertext = binascii.unhexlify(ciphertext)
	c_file = open(Vfile_save, 'wb+')
	c_file.write(ciphertext)
	c_file.close()

def AES_CBC(plaintext): 

	var = AES.new(key, AES.MODE_CBC, IV)

	if Vstart == 'Encriptar':

		ciphertext = var.encrypt(plaintext)
		ciphertext = binascii.hexlify(ciphertext)
		ciphertext = ciphertext.decode('utf8')

	elif Vstart == 'Decriptar':

		ciphertext = binascii.unhexlify(plaintext)
		ciphertext = var.decrypt(ciphertext)
		ciphertext = ciphertext.decode('utf8')		

	ciphertext = binascii.unhexlify(ciphertext)
	c_file = open(Vfile_save, 'wb+')
	c_file.write(ciphertext)
	c_file.close()


## # # # # # # # # # # # # # # #

# - - - Interação Usuário- - - #

## # # # # # # # # # # # # # # #

while(True):


# # # # # # # # # # # # # # # # # # #

# - - - Operação, sair e modo - - - #

# # # # # # # # # # # # # # # # # # #

	Vstart = start()
	if Vstart == 'Sair':
		exit()
	Vmode = mode()
	

# # # # # # # # # # # # # # # # # #

# - - - Instanciar variaveis - - -#

# # # # # # # # # # # # # # # # # #

	Vkey_size = 'NULL'
	Vkey_open = 'NULL'
	key = 'NULL'


# # # # # # # # # # # # # # # # # # # # # # # # # #

# - - - Encriptar, Nova Chave, Decriptar... - - - #

# # # # # # # # # # # # # # # # # # # # # # # # # #

	if Vstart == 'Encriptar':
		Vk_or_p = k_or_p()

		if Vk_or_p == 'Nova Chave':
			Vkey_size = key_size()
			Vkey_save = key_save()
			Vkey_open = Vkey_save

			key_output(Vkey_size, Vkey_save)
			key = key_input(Vkey_open)

		elif Vk_or_p == 'Chave Existente':
			Vkey_open = key_open()
			key = key_input(Vkey_open)

		elif Vk_or_p == 'Senha':
		    key = password()
		    #key = binascii.hexlify(key)

	elif Vstart == 'Decriptar':
		Vk_or_p2 = k_or_p2()

		if Vk_or_p2 == 'Chave Existente':
		    Vkey_open = key_open() 		    
		    key = key_input(Vkey_open)

		elif Vk_or_p2 == 'Senha':
		    key = password()
		    #key = binascii.hexlify(key)


# # # # # # # # # # # # #

# - - - Modo e IV - - - #

# # # # # # # # # # # # #

	if Vmode == 'CBC':
		VIV_exist = IV_exist()
		if VIV_exist == 'Novo IV':
			VIV_save = IV_save()	
			VIV_open = VIV_save		
			
			key_output(128, VIV_save)			
			IV = key_input(VIV_open)

		elif VIV_exist == 'IV Existente':
			VIV_open = IV_open()
			IV = key_input(VIV_open)


## # # # # # # # # # # # # # # #

# - - - Carregar Arquivo - - - #

## # # # # # # # # # # # # # # #

	Vfile_open = file_open()
	Vfile_save = file_save()


## # # # # # # # # # # # # # #

# - - - Carregar texto - - - #

## # # # # # # # # # # # # # #

	file = open(Vfile_open,'rb')
	
	plaintext = file.read()

	plaintext = binascii.hexlify(plaintext)

	Vfile_open = tar_pad(plaintext, Vfile_open)

	file.close()

	file = open(Vfile_open,'rb')
	
	plaintext = file.read()

	plaintext = binascii.hexlify(plaintext)

	dic = {'ECB':AES_ECB, 'CBC':AES_CBC}

	dic[Vmode](plaintext) 

	os.system('rm pln.tar')


# # # # # # # # # # # # # # # # 

# - - - - - - FIM - - - - - - #

# # # # # # # # # # # # # # # #