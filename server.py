from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Função para simular o botão sendo pressionado (sem Arduino físico)
def simular_botao(key):
    print(f'Comando simulado do botão pressionado: {key}')
    time.sleep(0.1)

@app.route('/send-key', methods=['POST'])
def send_key():
    data = request.get_json()
    key = data.get('key')

    if key:
        try:
            simular_botao(key)  # Simula o pressionamento do botão no Arduino
            return jsonify({'message': f'Comando "{key}" simulado'}), 200
        except Exception as e:
            return jsonify({'message': f'Erro ao simular o comando: {str(e)}'}), 500
    else:
        return jsonify({'message': 'Comando não especificado'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Rodando na porta 5001
