#Programa de control de Hogar Domotica

from sys import exit
import psycopg2
from bd_conexion import conexion
    
def distinct():
    try:
        with conexion.cursor() as cursor:
            sql="select distinct tipo from elementos"
            cursor.execute(sql)
            Data=[]
            for row in cursor:
                 Data.append(row[0])
            return Data     
    except psycopg2.Error as e:
            print("Ocurrió un error con la Base de Datos: ", e)
    
class BD_Select():
    def __init__(self,Element_type):
        self.Element_type = Element_type
        try:
            with conexion.cursor() as cursor:
                sql="select * from elementos where tipo='%s'" % self.Element_type
                cursor.execute(sql)
                print ("El estado de las %s es el siguiente" % self.Element_type)
                for x in cursor:
                    print ("\tEl elemento %s tiene el estado %s" % (x[1],x[2]))
    
                Question = str(input("Desea cambiar el estado de algun elemento Si (s) o No (n)?:"))
                if Question =="s" or Question == "si":
                    Question2 = str(input("Indique el nombre del elemento a cambiar!:"))
                    BD_Update(self.Element_type, Question2)
                else:
                    print("Hasta luego")
        except psycopg2.Error as e:
            print("Ocurrió un error con la Base de Datos: ", e)
        
class BD_Update():
    def __init__(self, Element_type, Element_name):
        self.Element_name = Element_name
        self.Element_type = Element_type
        try:
            with conexion.cursor() as cursor:
                sql="select estado from elementos where nombre='%s' and tipo='%s'" % (self.Element_name, self.Element_type)
                cursor.execute(sql)
                for fila in cursor:
                    state=str(fila[0])
                if state=="False":
                    sql="update elementos set estado='%s' where nombre='%s' and tipo='%s'" % ("true",self.Element_name, self.Element_type)
                    print("\tValor cambiado a True")
                else:
                    sql="update elementos set estado='%s' where nombre='%s' and tipo='%s'" % ("false",self.Element_name, self.Element_type)
                    print("\tValor cambiado a False")
                print("Hasta luego")
                cursor.execute(sql)
                conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error con la Base de Datos: ", e)
ElementsControl=[]
ElementsControl=distinct()
print ("Por favor indique que elemento desea monitorear")
for x in ElementsControl:
    msj = str(x)
    print ("\t %s (%s)" % (x,msj[0:1]))
    
action = input("\nPuedes colocar el nombre o la inicial: ")
if action == ElementsControl[0] or action == "L":
    BD_Select("Luces") 
elif action == ElementsControl[1] or action == "P":
    BD_Select("Puertas")
elif action == ElementsControl[2] or action == "E":
    BD_Select("Equipos")
elif action == ElementsControl[3] or action == "A":
    BD_Select("Alarmas")
else:
    print ("Introdujo un valor errado")

conexion.close()