from User import*


class AlmacenamientoUser:

    listaUser=[]
    listaGeneralUser=[]

    def registrarUser(self,user):

        self.listaUser.append(user)
        lista=[]
        lista.append(user.username)
        lista.append(user.nombre)
        lista.append(user.apellido)
        lista.append(user.telefono)
        lista.append(user.contrasena)
        lista.append(user.correo)
        lista.append(user.tipo)
        print(lista)
        print(user)
        print(type(user))

        self.listaGeneralUser.append(lista)

        print(f"Usuario {user.username} registrado con exito!")
        return f"Usuario {user.username} registrado con exito!"

    def eliminarUser(self,username):
        print(username)
        user=self.consultarUserPorUsername(username)
        if(user!=None):
            nombre=user.username
            for i in range(len(self.listaGeneralUser)):
                lista=self.listaGeneralUser[i]
                print("-->",lista)
                if(user.username==lista[0]):
                    print("Elimina")
                    self.listaGeneralUser.remove(lista)
                    self.listaUser.remove(user)
                    break
            
        return f"El estudiante {nombre} Se ha eliminado con exito!"

    def actualizarUser(self,miUser):
        user=self.consultarUsuarioPorUsername(miUser.username)
        mensaje=""
        if(user!=None):
            user.nombre=user.nombre
            user.apellidos=user.apellidos
            user.telefono=user.telefono
            user.correo=user.correo
            self.actualizarListageneral(user)
            mensaje="se ha actualizado el usuario"
        else:
            mensaje="el usuario no se pudo actualizar"
        return mensaje

    def actualizarListageneral(self,username):
        for i in range(len(self.listaGeneralUser)):
            lista=self.listaGeneralUser[i]
            print("-->",lista)
            if(username.username==lista[0]):
                print("Actualiza")
                lista[1]=username.nombre
                lista[2]=username.apellidos
                lista[3]=username.telefono
                lista[4]=username.correo
                if (username.tipo==1):
                    print("Ingresa a tipo 1")
                    lista[5]="Administrador"
                else:
                    lista[5]="Usuario"
                    print("Ingresa a tipo 2")
                
                break


    def obtenerListaUser(self):
        print(self.listaGeneralUser)
        return self.listaGeneralUser

    def consultarUsuarioPorCorreo(self,correo):
        usuario=None 
        if(self.validaTamanioLista()==True):
            for usu in self.listasUsuarios:
                if(usu.correo==correo):
                    usuario=usu
        
        return usuario

    def consultarListaUser(self):
        if(self.validaTamanioLista()==True):
            for i in range(len(self.listaUser)):
                user=self.listaUser[i]
                print(user)
        
        return self.listaUser


    def consultarUserPorUsername(self,username):
        user=None
        if(self.validaTamanioLista()==True):
            for est in self.listaUser:
                if(est.username==username):
                    user=est

        return user

    def consultarResultados(self,resultado):
        cant=0
        if(self.validaTamanioLista()==True):
            for est in self.listaUser:
                if(est.resultado==resultado):
                    cant+=1
        
        return cant

    def obtenerCantidadUser(self):
        return len(self.listaUser)

    def validaTamanioLista(self):
        if(len(self.listasUsuarios)>0):
            return True
        else:
            print("\n<<<< No han registrado usuario >>>")
            return False