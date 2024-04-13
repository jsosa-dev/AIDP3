from flask import Flask, jsonify
import platform
import sys
import subprocess

sistemaop = sys.platform
sistema = platform.system()
version = platform.release()
hostname = platform.node()
cpu = platform.processor()

app = Flask(__name__)


if(sistema == "Windows"):
    local = subprocess.getoutput("""for /f "tokens=2 delims==[]" %a in ('ping -n 1 -4 "%computername%"') do echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")

diccionario = {'ip':local,'so':sistema,'version':version,'hostname': hostname,'cpu': cpu}

@app.route('/info', methods=['GET'])
def get_tasks():
    return jsonify(diccionario)

if __name__ == '__main__':
    app.run(debug=True)