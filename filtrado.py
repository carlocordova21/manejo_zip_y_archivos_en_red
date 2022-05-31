from datetime import datetime
import subprocess
import os
from dotenv import load_dotenv
load_dotenv()

# Inicializacion de variables
conexion = os.getenv('CONEXION')
ruta_acceso = os.getenv('RUTA_ACCESO')
user_acceso = os.getenv('USER_ACCESO')
pass_acceso = os.getenv('PASS_ACCESO')
fecha_hoy = datetime.today().strftime('%Y%m%d')[2:]
fecha_busqueda = '220528' # Formato fecha: 220530

subprocess.getoutput('net use {0} {1} "{2}" /user:{3}'.format(conexion, ruta_acceso, pass_acceso, user_acceso))

os.chdir(conexion)
command = 'dir /b *{0}*.zip *{1}*.rar'.format(fecha_busqueda, fecha_busqueda)
output = subprocess.getoutput(command)

lista_zip = output.split('\n')
print(lista_zip)
# os.system('net use {0} {1} "{2}" /user:{3}'.format(conexion, ruta_acceso, pass_acceso, user_acceso))