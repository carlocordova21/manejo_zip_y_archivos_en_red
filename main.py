import subprocess
password = '{password}'
ruta_archivo = '{ruta_archivo}'
ruta_zip = '{ruta_zip}'

command = '7z a -p{0} "{1}" "{2}"'.format(password, ruta_zip, ruta_archivo)
subprocess.call(command, shell=True)