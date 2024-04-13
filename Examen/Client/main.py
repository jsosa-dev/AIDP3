from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/home')
def get_trivia_questions():
    response = requests.get('http://127.0.0.1:5000/info')
    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', data=data)
    else:
        return "Error al obtener datos", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)