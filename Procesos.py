from User import*
from AlmacenamientoUser import*

class Procesos:
    
    user=User()
    usuarioGlobal=None
    miAlmacenamientoUser=AlmacenamientoUser()

    def establecerUser(self,user):
        self.usuarioGlobal=user

    def registrarUser(self,miUser):
        print("Usuario a registrar", miUser)
        return self.miAlmacenamientoUser.registrarUser(miUser)

    def consultarUsuario(self,correo):
        usuario=self.miAlmacenamientoUser.consultarUsuarioPorCorreo(correo)

        if(usuario!=None):
            print(usuario)
        else:
            print(f"\nNo existe ningún estudiante con el documento {correo}")
            
        return usuario


    def actualizarUser(self,miUser):
        return self.miAlmacenamientoUser.actualizarUser(miUser)

    def eliminarUser(self,username):
        return self.miAlmacenamientoUser.eliminarUser(username)

    def consultarUser(self,username):
        user=self.miAlmacenamientoUser.consultarUserPorUsername(username)

        if(user!=None):
            print(user)
        else:
            print(f"\nNo existe ningún usuario con el nomnbre {username}")

        return user

    def obtenerListaUser(self):
        lista=self.miAlmacenamientoUser.obtenerListaUser()  
        return lista

    def consultarListaUser(self):    
        print("\n<<<<<<<<<<<<<<<<<- LISTA DE USUARIOS ->>>>>>>>>>>>>>>>>>>>")
        self.miAlmacenamientoUser.consultarListaUser()  
        print("\n*************************************************************\n")

#