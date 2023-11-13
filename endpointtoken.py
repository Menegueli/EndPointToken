from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

app = Flask(__name__)

@app.route('/cotacao-bitcoin', methods=['GET'])
def obter_cotacao_bitcoin():
    # Obtém o token da variável de ambiente
    api_token = os.getenv('API_TOKEN')

    # Verifica se o token está presente
    if not api_token:
        return jsonify({'error': 'Token não configurado'}), 500

    api_url = f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl&api_key={api_token}'

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Falha na requisição à API'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
