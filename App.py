from flask import Flask, request, jsonify

app = Flask(__name__)

def responder(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem:
        return "Olá! Eu sou o Apolo 🚀"
    elif "hora" in mensagem:
        import datetime
        return datetime.datetime.now().strftime("Agora são %H:%M")
    else:
        return "Ainda estou aprendendo..."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    resposta = responder(data["mensagem"])
    return jsonify({"resposta": resposta})

@app.route("/")
def home():
    return "Apolo online 🚀"

if __name__ == "__main__":
    app.run()
