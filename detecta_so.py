import platform
import sys
import subprocess

sistemaop = sys.platform
sistema = platform.system()
version = platform.release()
hostname = platform.node()
cpu = platform.processor()

print("Estamos en {}: ".format(sistema), "en version: {}".format(version))
print("Tipo SO: {}".format(sistemaop))

if(sistema == "Windows"):
    print("")
    #local = subprocess.getoutput("""for /f "tokens=2 delims==[]" %a in ('ping -n 1 -4 "%computername%"') do echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    print("Hostname: ", hostname)
    print("CPU: ", cpu)
print(local)




