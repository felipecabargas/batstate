#! /usr/bin/python
# 2011-2012 | Created by Alfonso Cabargas Madrid under GPL 3 License
# 2014      | 		     Katerine Munoz Tello
# Please visit http://www.cabargas.com/ for more info about this program.
# Any question drop me an email to <felipe@cabargas.com>

import os
import math

print "Estado de desgaste bateria - by @juanpintoduran and @milkshakecroc"

def backward(linea):
	llista = list(linea)
	nlist = list(reversed(llista))
	new_list = list(reversed(nlist[5:9]))
	return new_list[0]+new_list[1]+new_list[2]+new_list[3]

lista = list()
if os.path.exists('/proc/acpi/battery/BAT1/')==True:
	bat = open('/proc/acpi/battery/BAT1/info', 'r')
	for status in bat.readlines():
		lista.append(status)
design = int(backward(lista[1]))
last_full = int(backward(lista[2]))

if design == status:
	desgaste = 0
else:
	desgaste = last_full*100/design
print "El porcentaje de desgaste de tu bateria BAT1 es : "+str(desgaste)+'%'

