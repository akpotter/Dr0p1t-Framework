#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
from urllib.request import urlopen
from .color import *
from . import color
import os

def check():
	response = urlopen('https://raw.githubusercontent.com/D4Vinci/Dr0p1t-Framework/master/core/version.txt')
	version = response.read().decode('utf-8').strip()
	f = open( os.path.join("core","version.txt"), 'r')
	file_data = f.read().strip()
	if version != file_data:
		colored_print('\n[*] New Version available ! Visit: https://github.com/D4Vinci/Dr0p1t-Framework\n',"y")
	else:
		pass
		colored_print('[*] Your version is up-to-date ;)',"b")
