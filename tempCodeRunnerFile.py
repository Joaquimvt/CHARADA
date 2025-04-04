from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Lista de charadas sobre futebol
charadas = [
     {
        "id": 1,
        "pergunta": "O que é, o que é? Tem chaves, mas não abre portas.",
        "resposta": "O teclado."
    },
    {
        "id": 2,
        "pergunta": "O que é, o que é? Tem pernas, mas não anda.",
        "resposta": "A mesa."
    },
    {
        "id": 3,
        "pergunta": "O que é, o que é? Quanto mais se tira, maior fica.",
        "resposta": "O buraco."
    },
    {
        "id": 4,
        "pergunta": "O que é, o que é? Tem um banco, mas não senta.",
        "resposta": "O banco de areia."
    },
    {
        "id": 5,
        "pergunta": "O que é, o que é? Cai de pé e corre deitado.",
        "resposta": "A chuva."
    },
    {
        "id": 6,
        "pergunta": "O que é, o que é? Tem bico e não canta.",
        "resposta": "O bule."
    },
    {
        "id": 7,
        "pergunta": "O que é, o que é? Tem coroa, mas não é rei.",
        "resposta": "O abacaxi."
    },
    {
        "id": 8,
        "pergunta": "O que é, o que é? Sempre se quebra quando se fala.",
        "resposta": "O segredo."
    },
    {
        "id": 9,
        "pergunta": "O que é, o que é? Não pode ser usado antes de ser quebrado.",
        "resposta": "O ovo."
    },
    {
        "id": 10,
        "pergunta": "O que é, o que é? Tem dentes, mas não morde.",
        "resposta": "O pente."
    }
]


@app.route('/')
def index():
    # Escolhe uma charada aleatória
    charada_aleatoria = random.choice(charadas_futebol)
    return render_template('index.html', charada=charada_aleatoria)

@app.route('/nova_charada')
def nova_charada():
    # Escolhe uma nova charada aleatória
    charada_aleatoria = random.choice(charadas_futebol)
    return render_template('index.html', charada=charada_aleatoria)

if __name__ == '__main__':
    # Define a porta como 5003
    app.run(debug=True, port=5003)
