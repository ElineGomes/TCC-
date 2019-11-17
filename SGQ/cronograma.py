
#Importa MicroFramework para Apps Versão = 0.12.2
#Importa renderização de HTML

from flask import Flask, render_template, request, redirect, session
from dao import lista_atividades

app = Flask(__name__)
app.secret_key = 'admin'
lista = []

for i in [1,2,3,4]:
    id_processo_atividade = i
    processo = ""
    atividade = ""
    tempo = 0
    lista.append(lista_atividades(id_processo_atividade, processo, atividade, tempo))

@app.route('/')
def index():
    #if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #    return redirect('/login')
    return render_template('cronograma.html', titulo='Login', atividades=lista)

#Define pagina inicial de login
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
#    usuario = request.form['nome']
#    senha = request.form['senha']
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + 'logou com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect('/')

app.run()