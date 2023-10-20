#importando el modelo con el cual se va a trabajar
from .models import Student 
#importando el serializador correspondiente al modelo para convertir la informacion a json
from . serializers import StudentSerializer
#importando la libreria para enviar la respuesta
from rest_framework.response import Response
#importando el decorador para poder trabajar con los metodos http
from rest_framework.decorators import api_view
#Creating the apiview class
from django.contrib.auth.models import User 
from rest_framework import BaseAuthentication

#se añaden los metodos que utilizara la funcion
@api_view(['GET','POST', 'PUT'])
    #defining the get method of StudentAPIView
def students_api_view (request):
    #si el metodo es get(obtener o leer informacion)
    if request.method == 'GET':
        #se recuperan los datos de la bdd
        student =  Student.objects.all()
        #se serializan los datos y si son varios datos a serializar se establece el parametro many en true
        students_serializer = StudentSerializer(student, many = True)
        #se retorna el serializador con su propiedad .data
        return Response(students_serializer.data)
    #caso contrario de que se desee crear una instancia ("Se utilice el metodo POST")
    elif request.method == 'POST':        
        #Se serializan los datos que vienen de la peticion 
        student_serializer = StudentSerializer(data = request.data)
        #si los datos son validos se guardan, sino retorna error 
        if student_serializer.is_valid():
            #guardando 
            student_serializer.save()
        return Response(student_serializer.data)
    return Response(student_serializer.errors)


#vista para el caso de actualizar ("PUT") o eliminar ("DELETE)
#se obtiene primero el dato requerido filtrando por llave primaria, de esta manera no se modificaran todos los datos
@api_view(['PUT','GET','DELETE'])
def students_datail_api_view(request, pk = None):
    if request.method == 'GET':
        #filtrando el objeto por llave primaria 
        student = Student.objects.filter(id = pk).first()
        #se serializan 
        student_serializer = StudentSerializer(student)
        #se retornan en forma de dict
        return Response(student_serializer.data)
    #caso de actualizar
    elif request.method == 'PUT':
        #se escoge el objeto a modificar
        student = Student.objects.filter(id = pk).first()
        #se serializa
        student_serializer = StudentSerializer(student, data = request.data)
        #si la peticion es valida("lo que se quiere actualizar esta correcto")
        if student_serializer.is_valid():
            #se guarda en la bdd
            student_serializer.save()
            #Se retorna 
            return Response(student_serializer.data)
        return Response (student_serializer.errors)
    # En el caso de eliminar 
    elif request.method == 'DETELE':
        #se escoge el objeto a eliminar 
        student = Student.objects.filter(id = pk).first()
        #se borra
        student.delete()
        # la respuesta
        return Response('ELIMINADO CON EXITO')
    
class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_username')
        if not username:
            return None
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such User')
    
        return (user,None)
    
