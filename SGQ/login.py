from flask_bootstrap import Bootstrap
from os import path
from flask import Flask
#from .blueprints.noticias import noticias_blueprint
from flask_bootstrap import Bootstrap

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

def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )

    app = Flask("wtf",
                instance_path=instance_path,
                instance_relative_config=True)

    app.config.from_object('wtf.default_settings')
    app.config.from_pyfile('config.cfg')

    app.config['MEDIA_ROOT'] = path.join(
        app.config.get('PROJECT_ROOT'),
        app.instance_path,
        app.config.get('MEDIA_FOLDER')
    )

    app.register_blueprint(noticias_blueprint)

    Bootstrap(app)
    return app