from User import*
from Procesos import *


class Almacenamiento:

    procesos=Procesos()

    listaGeneral=[]
    listasUsuarios=[{
        "username":'Mooncake',
        "nombre":'Samuel',
        "apellido":'Rodriguez',
        "telefono":'3012105346',
        "contrasena":'admin',
        "correo":'pet@care',
        "tipo":'Usuario'
    }]
    correo=""

    def __init__(self):
        pass

    def actualizarUsuarios(self,user):
        for i in self.listasUsuarios:
            if(i["correo"]==user['correo']):
                i['username']=user['username']
                i['nombre']=user['nombre']
                i['apellido']=user['apellido']
                i['telefono']=user['telefono']

                return i

        return False



    def consultarUserPorUsername(self,correo,password):
            
        for i in self.listasUsuarios:
            if(i["correo"]==correo):
                if(i["contrasena"]==password):
                    self.correo=correo
                    return True
    
        return False


    def consultarUser(self):
            
        for i in self.listasUsuarios:
            if(i["correo"]==self.correo):
                    return i
                    
        return False

    def consultarUserV2(self,correo):
            
        for i in self.listasUsuarios:
            if(i["correo"]==correo):
                    return i
                    
        return False

    def registrarUsuarios(self,usuario):
        
        self.listasUsuarios.append(usuario)

        print(f"{usuario['username']} ha sido registrado con exito")

    def eliminarUsuario(self,username):
        print(username)
        usuario=self.consultarUsuarioPorUsername(username)
        if(usuario!=None):
            nombre=usuario.nombre
            for i in range(len(self.listaGeneral)):
                lista=self.listaGeneral[i]
                print("-->",lista)
                if(usuario.username==lista[0]):
                    print("Elimina")
                    self.listaGeneral.remove(lista)
                    self.listasUsuarios.remove(usuario)
                    break
        
        return f"El estudiante {nombre} Se ha eliminado con exito!"



    def validaTamanioLista(self):
        if(len(self.listasUsuarios)>0):
            return True
        else:
            print("\n<<<< No han registrado usuario >>>")
            return False