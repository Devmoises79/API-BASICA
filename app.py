from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'Título': 'Pai Rico, Pai Pobre',
        'Autor': 'Robert Kiyosaki e Sharon L. Letcher',
    },
    
    {
        'id': 2,
        'Título': 'A arte da guerra',
        'Autor': 'Sun Sutzu',
    },
    
    
    {
        'id': 3,
        'Título': 'Por Que Escrevo',
        'Autor': 'George Orwell',
    },
    
    
    {
        'id': 4,
        'Título': 'Economia Básica',
        'Autor': 'Thomas Sowell',
    }
]


@app.route('/livros', methods=['GET'])
def obtendo_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if  livro.get('id') == id:
            return jsonify(livro)
    
@app.route('/livros/<int:id>', methods=['PUT'])
def edit_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(novo_livro)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
            return jsonify(livros)
            

app.run(port=5000, host='localhost', debug=True)