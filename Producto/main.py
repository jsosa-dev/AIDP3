from flask import Flask, render_template, request, jsonify
import requests
from googletrans import Translator

app = Flask(__name__)

# Endpoint para obtener preguntas de trivia en español
@app.route('/trivia')
def get_trivia_questions():
    # Parámetros de la solicitud HTTP a la API de Trivia
    parameters = {
        'amount': 1,  # Número de preguntas a obtener
        'category': 9,  # Categoría de las preguntas (9 es General Knowledge)
        'type': 'multiple'  # Tipo de preguntas (multiple choice)
    }

    # Realizar la solicitud HTTP a la API de Trivia
    response = requests.get('https://opentdb.com/api.php', params=parameters)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener las preguntas en formato JSON
        questions_json = response.json()

        # Traducir las preguntas al español utilizando Google Translate
        for question in questions_json['results']:
            question['question'] = translate_to_spanish(question['question'])
            question['incorrect_answers'] = [translate_to_spanish(ans) for ans in question['incorrect_answers']]
        
        # Devolver las preguntas traducidas y renderizar la plantilla HTML
        return render_template('trivia.html', question=questions_json['results'][0]['question'], 
                                            options=questions_json['results'][0]['incorrect_answers'] 
                                            + [questions_json['results'][0]['correct_answer']])
    else:
        # Devolver un mensaje de error si la solicitud falló
        return jsonify({'error': 'No se pudo obtener las preguntas de trivia.'}), 500

# Endpoint para verificar la respuesta del usuario
@app.route('/check_answer', methods=['POST'])
def check_answer():
    # Obtener la respuesta seleccionada por el usuario
    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    if user_answer == correct_answer:
        return "¡Respuesta correcta!"
    else:
        return "Respuesta incorrecta. La respuesta correcta es: " + correct_answer

def translate_to_spanish(text):
    # Inicializar el traductor
    translator = Translator()

    # Traducir el texto al español
    translation = translator.translate(text, src='en', dest='es')

    # Devolver el texto traducido
    return translation.text

if __name__ == '__main__':
    app.run(debug=True) # Ejecutar la aplicación en modo de depuración