import platform
import sys
import subprocess
import json

sistemaop = sys.platform
sistema = platform.system()
version = platform.release()
hostname = platform.node()
cpu = platform.processor()

if(sistema == "Windows"):
    local = subprocess.getoutput("""for /f "tokens=2 delims==[]" %a in ('ping -n 1 -4 "%computername%"') do echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")

diccionario = {'ip':local,'so':sistema,'version':version,'hostname': hostname,'cpu': cpu}

dictionaryToJson = json.dumps(diccionario)
print(dictionaryToJson)
file=open("data.json", "w")
json.dump(diccionario, file, indent=4)
file.close()



