from flask import Flask, render_template, request
from flask.wrappers import Response
from Procesos import*
from User import*
from Almacenamiento import *

app = Flask(__name__)

almacenamiento=Almacenamiento()
titulos=("Nombre","Apellidos","Telefono","correo")
titulosTablaUser=("Username","Nombre(s)","Apellidos","Telefono","Correo","Tipo")

misProcesos=Procesos()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/registrar")
def registro():
    return render_template('registro_usuario.html')

@app.route("/consultar")
def consulta():
    informacion=misProcesos.obtenerListaUser()
    print(almacenamiento.registrarUsuarios)
    user=almacenamiento.consultarUser()
    print(user)
    return render_template("consulta.html",titulos_tabla=titulosTablaUser,data=informacion,user=user)

@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():
    mensaje=""
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        response=almacenamiento.consultarUserPorUsername(correo,contrasena)
        if(response==True):
            return render_template("inicio.html")

        else:
            mensaje='Usuario o contraseña incorrecto'
            print("Usuario o contraseña incorrecto")

    return render_template('index.html',correo=None,mensaje=mensaje)

@app.route("/pagina")
def pagina():
    return render_template("pagina.html")



@app.route("/registro_usuario", methods=['GET', 'POST'])
def registrarUser():
    msj=""
    user={
        "username":request.args.get('username'),
        "nombre":request.args.get('nombre'),
        "apellido":request.args.get('apellido'),
        "telefono":request.args.get('telefono'),
        "contrasena":request.args.get('contrasena'),
        "correo":request.args.get('correo'),
        "tipo":request.args.get('tipo')
    }
    almacenamiento.registrarUsuarios(usuario=user)
    
    resultado=None
    username,nombre,apellido,telefono,contrasena,correo,tipo="","","","","","",""

    if request.method == 'POST':
        user=None
        username=request.form['username']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        telefono=request.form['telefono']
        contrasena=request.form['contrasena']
        correo=request.form['correo']
        tipo=request.form['tipo']

        print("Registrar")
            
        user=misProcesos.consultarUser(username)
        if user==None:
            user=User(username,nombre,apellido,telefono,contrasena,correo,tipo)
            print(user)
            misProcesos.registrarUser(user)
            resultado=misProcesos.registrarUser(user)
            print(resultado)

        else:
            resultado=f"El documento ya se encuentra registrado y corresponde a {user.nombre}"       
            print(resultado)

    msj='Has sido registrado con exito'

    return render_template('registro_usuario.html',mensaje=msj)

@app.route("/obtener_usuario", methods=['GET'])
def obtener_usuario():
    correo=request.args.get('correo')
    print(correo)
    respuesta=almacenamiento.consultarUserV2(correo)
    print(respuesta)

    return render_template("gestionUsuario.html",usuario=respuesta)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    print("Actualización")
    print(request.form['apellido'])
    diccionario_actualizar={
        "correo":request.form['correo'],
        "username":request.form['username'],
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "telefono":request.form['telefono'],
    }
    print(diccionario_actualizar)
    actualizacion=almacenamiento.actualizarUsuarios(diccionario_actualizar)
    print(actualizacion)

    return render_template('gestionUsuario.html', usuario=actualizacion)

@app.route("/eliminar_usuario", methods=['POST'])
def eliminar_usuario():
    print(almacenamiento.registrarUsuarios)
    


@app.route("/registro_clinica")
def registro_clinica():
    return render_template('registro_clinica.html',user=Procesos.usuarioGlobal)

@app.route("/form")
def form():
    return render_template('form.html')
    
@app.route("/enviar_datos")
def enviar_datos():
    return render_template('index.html')

@app.route("/inicio")
def inicio():
    user=almacenamiento.consultarUser()
    return render_template('inicio.html',user=user)
    

@app.route('/gestion_clinicas')
def gestion_Simple():
    return render_template('gestionClinicas.html')

@app.route('/gestion_usuario')
def gestion_usuario():
    return render_template("gestionUsuario.html")

@app.route("/gestion_user")
def gestion_user():
    return render_template("gestionar_user.html",user=Procesos.usuarioGlobal)


if (__name__ == '__main__'):
    app.run(debug=True,port=5000)