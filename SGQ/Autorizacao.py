#Página de autorização de acesso para Gestão de Qualidade

#Importa MicroFramework para Apps Versão = 0.12.2
#Importa renderização de HTML
from flask import Flask, render_template, request, redirect, session, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'admin'

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
    flash('Nenhum usuário logado!')
    return redirect('/')


#Executa a aplicação - Trocar host e porta para produção
#templates.run(host='0.0.0.0', port=8080)
app.run()