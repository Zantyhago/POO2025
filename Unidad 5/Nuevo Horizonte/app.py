from flask import Flask, render_template, request, flash, redirect
from models import db, Trabajador, RegistroHorario
from datetime import date, time, datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def inicio():
    return render_template('Inicio.html')

@app.route('/RegistraEntrada', methods = ['GET', 'POST'])
def RegistraEntrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        digitos = request.form['dig']
        dependencia = request.form['dependencia']
        xfecha = date.today()
        worker = Trabajador.query.filter_by(legajo = legajo).first()
        if not worker:
            return render_template ('aviso.html', mensaje = 'No se encontró el trabajador ingresado.')
        if worker.dni[-4:] != digitos:
            return render_template ('aviso.html', mensaje = f'{worker.apellido} {worker.nombre} no posee el DNI ingresado.')
        entradaExiste = RegistroHorario.query.filter_by(idtrabajador = worker.id, fecha = xfecha).first()
        if entradaExiste:
            return render_template ('aviso.html', mensaje = f'Hoy {xfecha} {worker.apellido} {worker.nombre} ya ingresó.')
        entradaNueva = RegistroHorario(
            idtrabajador = worker.id,
            fecha = xfecha,
            horaentrada = datetime.now().time(),
            dependencia = dependencia)
        db.session.add(entradaNueva)
        db.session.commit()
        return render_template ('aviso.html', mensaje = f'Registro de entrada exitoso para {worker.apellido} {worker.nombre}.')
    return render_template('RegistraEntrada.html')

@app.route('/RegistraSalida', methods = ['GET', 'POST'])
def RegistraSalida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        digitos = request.form['dig']
        xfecha = date.today()
        worker = Trabajador.query.filter_by(legajo = legajo).first()
        if not worker:
            return render_template ('aviso.html', mensaje = 'No se encontró el trabajador ingresado.')
        if worker.dni[-4:] != digitos:
            return render_template ('aviso.html', mensaje = f'{worker.apellido} {worker.nombre} no posee el DNI ingresado.')
        entradaExiste = RegistroHorario.query.filter_by(idtrabajador = worker.id, fecha = xfecha).first()
        if entradaExiste:
            if not entradaExiste.horasalida:
                xhora = datetime.now().time()
                entradaExiste.horasalida = xhora
                xdepe = entradaExiste.dependencia
                if xdepe == 'D01':
                    xdepe = 'Edificio Central'
                elif xdepe == 'D02':
                    xdepe = 'Talleres'
                elif xdepe == 'D03':
                    xdepe = 'Centro deportivo'
                db.session.commit()
                #return render_template ('ConfirmarSalida.html', depe = xdepe)
                return render_template ('aviso.html', mensaje = f'Registro de salida exitoso para {worker.apellido} {worker.nombre} con dependencia {xdepe}.')
            else:
                return render_template ('aviso.html', mensaje = f'Hoy {xfecha} {worker.apellido} {worker.nombre} ya se retiró.')
        else:
            return render_template ('aviso.html', mensaje = f'Hoy {xfecha} {worker.apellido} {worker.nombre} no ingresó.')
    return render_template('RegistraSalida.html')

@app.route('/ConsultarRegistro', methods = ['GET', 'POST'])
def ConsultarRegistro():
    if request.method == 'POST':
        legajo = request.form['legajo']
        digitos = request.form['dig']
        fechaI = request.form['fechaI']
        fechaF = request.form['fechaF']
        worker = Trabajador.query.filter_by(legajo = legajo).first()
        if not worker:
            return render_template ('aviso.html', mensaje = 'No se encontró el trabajador ingresado.')
        if worker.dni[-4:] == digitos:
            xregs = RegistroHorario.query.filter(
                RegistroHorario.idtrabajador == worker.id,
                RegistroHorario.fecha >= fechaI,
                RegistroHorario.fecha <= fechaF
            ).order_by(RegistroHorario.fecha).all()
            if xregs:
                xnombre = worker.apellido + ' ' + worker.nombre
                return render_template('Mostrador.html', registros = xregs, nombre = xnombre)
            else:
                return render_template ('aviso.html', mensaje = f'{worker.apellido} {worker.nombre} no posee registros en el período.')
        else:
            return render_template ('aviso.html', mensaje = f'{worker.apellido} {worker.nombre} no posee el DNI ingresado.')
    return render_template('/ConsultarRegistro.html')

'''@app.route('/ConfirmarSalida', methods = ['GET', 'POST'])
def ConfirmaSalida():
    if request.method == 'POST':
        xrespuesta = request.form['respuesta']
        if xrespuesta == 'no':
            return render_template ('aviso.html', mensaje = 'Intente registrar su salida nuevamente :c')
        elif xrespuesta == 'si':
            db.session.commit() #de estar mal re contra remil corregir
            return render_template ('aviso.html', mensaje = f'Registro de salida exitoso para {worker.apellido} {worker.nombre} las {xhora}.')
    return render_template('RegistraSalida.html')'''

if __name__ == '__main__':
    app.run(debug = True)