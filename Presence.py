import os
import json
import io
import time
import sys
import traceback
import pypresence

_default = {
    "client_id": "482647762400182283",
    "state": "Пишу код...",
    "details": "Мучаю бота...",
    "end": "$real",
    "start": "$real",
	"assets": {
    	"large_icon": "large",
    	"large_icon_text": None,
    	"small_icon": "python",
    	"small_icon_text": None,
    	"show_spectate_button": True,
    	"show_join_button": False
    },
}

	
def presence():
	try:
		fp = json.load(io.open('config.json', 'r', encoding='utf-8-sig'))
	except Exception as error:
		while True:
			a = input('[WARN] Обнаружена ошибка в файле "config.json"!\nЖелаете загрузить (и сохранить в файл) конфигурацию по умолчанию? (Y-Да/N-Нет)\n> ')
			if a.lower() == 'y':
				fp = json.dump(_default, io.open('config.json', 'w', encoding='utf-8'), indent=2)
				return sys.exit(0)
			elif a.lower() == 'n':
				return sys.exit(0)
	try:
		a = pypresence.Presence(fp['client_id'], pipe=0)
		a.connect()
		if fp['assets']['show_spectate_button'] == True: spec = 'hello_world!!'
		else: spec = None
		if fp['assets']['show_join_button'] == True: join = 'hello_world!!'
		else: join = None
		if fp['end'] == None:                 fp['end'] = None
		if fp['start'] == None:               fp['start'] = None
		if fp['end'] == '$real':              fp['end'] = time.time()
		if fp['start'] == '$real':            fp['start'] = time.time()
		a.update(large_image=fp['assets']['large_icon'], large_text=fp['assets']['large_icon_text'], state=fp['state'], details=fp['details'], small_image=fp['assets']['small_icon'], small_text=fp['assets']['small_icon_text'], end=fp['end'], start=fp['start'], spectate=spec, join=join)
	except Exception as error:
		return print('Возникла ошибка в создании RPC процесса Rich Presence. \nПроверьте правильность ввода данных.\n\nПодробности:\n{}'.format(traceback.format_exc()))
	print('Rich Presence запущен!')
	

if __name__ == '__main__':
	presence()
	exit_ = input('Чтобы выйти, нажмите [ENTER]')