#! /usr/bin/python
# 2011-2012 | Created by Alfonso Cabargas Madrid under GPL 3 License
# Please visit http://www.cabargas.com/ for more info about this program.
# Any question drop me an email to <felipe@cabargas.com>

import os
import re
import math

welcome = "Estado de desgaste bateria - by @juanpintoduran"
print welcome

if os.path.exists('/proc/acpi/battery/BAT0/')==True:
	os.access('/proc/acpi/battery/BAT0/info', os.R_OK)	
	print "El porcentaje de desgaste de tu bateria BAT0 es :"
	print "Terminado."
else:
	if os.path.exists('/proc/acpi/battery/BAT1/')==True:
		bat = open('/proc/acpi/battery/BAT1/info')
		for status in bat.readlines(): 
			design = re.search(r'\d{4}', status[2])
			status = re.search(r'\d{4}', status[3])
			if design == status:
				desgaste = 0
			else:
				desgaste = status.group()*100/design.group()
		print "El porcentaje de desgaste de tu bateria BAT1 es :"
		print desgaste

	else:	          
  		print "Terminado."
