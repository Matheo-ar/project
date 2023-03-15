from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, Length


class Registro(FlaskForm):
    Tipodoc = StringField('Tipo Documento', validators=[DataRequired()])
    Documento = StringField('Número Documento', validators=[
                            DataRequired(), Length(max=20)])
    Nombres = StringField('Nombres', validators=[
                          DataRequired(), Length(max=60)])
    Apellidos = StringField('Apellidos', validators=[
                            DataRequired(), Length(max=60)])
    Nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    Genero = StringField('Genero', validators=[DataRequired()])
    '''Email = StringField('Correo electrónico', validators=[
                        DataRequired(), Email()])'''
    Email = StringField('Correo electronico', validators = [DataRequired(), Email()] )
    Telefono = StringField('Teléfono', validators=[
                           DataRequired(), Length(max=10)])
    Direccion = StringField('Direccion', validators=[
                            DataRequired(), Length(max=60)])
    Rol = StringField('Tipo Usuario', validators=[DataRequired()])
    Contraseña = PasswordField('Contraseña', validators=[
                               DataRequired(), Length(max=60)])
    Submit = SubmitField('Registrar')


class Login(FlaskForm):
    Documento = StringField('No. Documento', validators=[
                            DataRequired(), Length(max=20)])
    Contraseña = PasswordField('Contraseña', validators=[
                               DataRequired(), Length(max=60)])
    Submit = SubmitField('Ingresar')


class Users(FlaskForm):
    Tipodoc = StringField('Tipo Documento: ', validators=[DataRequired()])
    Documento = StringField('No. Documento: ', validators=[
                            DataRequired(), Length(max=20)])
    Submit = SubmitField('Buscar')


class Categories(FlaskForm):
    IdCategoria = StringField('Id categoria', validators=[
                                  DataRequired(), Length(max=10)])
    NombreCategoria = StringField('Nombre categoría', validators=[
                                  DataRequired(), Length(max=45)])
