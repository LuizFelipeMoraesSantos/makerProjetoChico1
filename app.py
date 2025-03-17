from flask import Flask, request, jsonify

app = Flask(__name__)

# Respostas corretas
correct_answers = {
    "Pergunta 1": "a",  # Resposta correta para a pergunta 1
}

@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()  # Pega os dados enviados pelo frontend
    resposta = data.get('resposta')  # Resposta do usuário

    # Verifica se a resposta está correta
    if resposta == correct_answers["Pergunta 1"]:
        return jsonify({"resposta": resposta, "status": "correto"})
    else:
        return jsonify({"resposta": resposta, "status": "errado"})

@app.route('/reset', methods=['POST'])
def reset_quiz():
    return jsonify({"status": "Quiz resetado!"})
function sendAnswer(answer) {
    fetch('http://localhost:5001/send-key', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key: answer }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById("feedback").innerHTML = `<span class='status correct'>✔ Comando enviado ao Arduino!</span>`;
    })
    .catch((error) => {
        console.error('Erro ao enviar o comando:', error);
        document.getElementById("feedback").innerHTML = `<span class='status incorrect'>✖ Erro ao enviar o comando!</span>`;
    });
}

if __name__ == '__main__':
    app.run(debug=True)
