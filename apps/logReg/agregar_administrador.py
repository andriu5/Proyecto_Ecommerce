import argparse
import bcrypt

#TODO: agregar clase User de models.py 

def agregarAdmin(admin: dict):
    print('*'*100)
    print("Nombre:", admin["nombre"])
    print("Apellido:", admin["apellido"])
    print("Email:", admin["email"])
    print("Nivel de Usuario:", admin["nivel_usuario"])
    print('*'*100)
    # pw_hash = bcrypt.hashpw(admin["password"].encode(), bcrypt.gensalt()).decode()
    # nuevo_admin = User.objects.create(nombre=admin["nombre"], apellido=admin["apellido"], nivel_usuario=2, email=admin["email"], password=pw_hash)
    # print(f"Info: Nuevo administrador agregado a la base de datos.\n Nombre: {new_user.nombre} {new_user.apellido} | Email: {new_user.email}")

# Argumentos del script:
parser = argparse.ArgumentParser(description='''
Este escript sirve para agregar nuevos administradores a la aplicacion de Ecommerce.

Ejemplos:
python apps/logReg/agregar_administrador.py --nombre Juan --apellido Perez --email jp@mail.com --password jpadmin123
python apps/logReg/agregar_administrador.py -n Andres -a Alvear -e andres.alvear5@gmail.com -p 12345678
''',
usage='%(prog)s [OPTIONS]',
formatter_class = argparse.RawTextHelpFormatter)
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-n", "--nombre", help="Nombre del Usuario Administrador", type=str, required=True)
requiredNamed.add_argument("-a", "--apellido", help="Apellido del Usuario Administrador", type=str, required=True)
requiredNamed.add_argument("-e", "--email", help="email del Usuario Administrador", type=str, required=True)
requiredNamed.add_argument("-p", "--password", help="Password del Usuario Administrador", type=str, required=True)
args = parser.parse_args()

# diccionario con los campos necesarios para crear un usuario administrador en la base de datos
admin = {
    "nombre": args.nombre,
    "apellido": args.apellido,
    "email": args.email,
    "nivel_usuario": 2,
    "password": args.password,
}
#TODO: falta soportar la creacion de Administradores desde la funcion agregarAdmin()
agregarAdmin(admin)