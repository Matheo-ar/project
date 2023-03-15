from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import Registro, Login, Users, Categories
from flask_mysqldb import MySQL
from flask_login import login_manager, login_user, logout_user, login_required
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
import models
from flask_login import LoginManager


app = Flask(__name__)

try:
    # CONEXION A LA BD MYSQL
    app.config['MYSQL_HOST'] = 'localhost'  # 190.158.204.52
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'admin'
    app.config['MYSQL_DB'] = 'bd_escuela'

    mysql = MySQL(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    print('Conectado')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)

# SEMILLA PARA EL ENCRIPTAMIENTO
semilla = bcrypt.gensalt()

# Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/registro', methods=["GET", "POST"])
def signUp():
    if 'documento' in session:
        form = Registro()
        if request.method == 'POST':
            if form.validate_on_submit():
                Tipodoc = form.Tipodoc.data
                Documento = form.Documento.data
                Nombres = form.Nombres.data
                Apellidos = form.Apellidos.data
                Nacimiento = form.Nacimiento.data
                Genero = form.Genero.data
                Email = form.Email.data
                Telefono = form.Telefono.data
                Direccion = form.Direccion.data
                Rol = form.Rol.data
                Contraseña = generate_password_hash(form.Contraseña.data)
                # Validar que no exista el registro persona
                row = models.validar_persona(mysql, Documento)

                if row == None:
                    # Se crea un nuevo registro en persona
                    Nacimiento = str(Nacimiento).replace('-', '')
                    # Validamos el rol del registro
                    es_alumno = 0
                    es_acudiente = 0
                    es_colaborador = 0

                    if Rol == 'estudiante':
                        es_alumno = 1
                    elif Rol == 'acudiente':
                        es_acudiente = 1
                    else:
                        es_colaborador = 1

                    models.crear_persona(mysql, Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                                         Telefono, Direccion, es_alumno, es_acudiente, es_colaborador)
                    # Se crea un nuevo registro en usuario
                    Nom_usuario = Nombres+' '+Apellidos
                    models.crear_usuario(
                        mysql, Documento, Nom_usuario, Email, Telefono, Contraseña)
                    flash('Registro Creado Exitosamente', 'success')
                else:
                    flash('El usuario '+Documento+' ya existe', 'success')

            return render_template('Registro.html', form=form)
        else:
            return render_template('Registro.html', form=form)
    else:
       return redirect('/login')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            Documento = form.Documento.data
            # Validamos si el usuario existe
            row = models.validar_usuario(mysql, Documento)
            if row != None and check_password_hash(row[1], form.Contraseña.data):
                # Registra la session
                session['documento'] = request.form['Documento']
                session['privilegio'] = row[2]
                return redirect(url_for('home'))
            else:
                flash('El usuario o la contraseña no son validos', 'alert')
                return render_template('login.html', form=form)
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/usuarios')
def users():
    form = Registro()
    # form = Users()
    return render_template('users.html', form=form)


@app.route('/categorias')
def categories():
    form = Categories()
    # form = Categories()
    return render_template('categories.html', form=form)


@app.route('/crearCategoria')
def createCategories():
    form = Categories()
    # form = Categories()
    return render_template('createCategories.html', form=form)


@app.route('/protected')
# @login_required
def protected():
    if 'documento' in session:
        if session['privilegio'] == "A":
            return 'usted es administrador'
        else:
            return 'usted es usuario de operacion'
    else:
        return redirect('/login')


@app.route('/cerrarsesion')
def logout():
    logout_user()
    # Limpiamos la sesión
    session.clear()
    return render_template('logout.html')


@login_manager.user_loader
def load_user(user):
    return User.get(user)

# Manejo de errores


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_interno(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
