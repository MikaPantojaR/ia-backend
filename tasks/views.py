from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UserView(viewsets.ModelViewSet):
    #se importa el serializador
    serializer_class = UserSerializer
    #me da los endpoints para crear un CRUD para manejar con la base de datos
    queryset = User.objects.all()

    @csrf_exempt
    @staticmethod
   #crear un endpoint extra para validar todo el login
    def validateCredentials(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email)
            user = User.authenticate(email, password)
            if user is not None:
                mensaje = f"Credenciales válidas"
                return JsonResponse({'mensaje': mensaje, 'rol': user.rol, 'nombre': user.nombre, "email": user.email, "diabetes": user.diabetes}, status=200)
            else:
                return JsonResponse({'mensaje': 'Credenciales inválidas'}, status=400)  #el usuario mando algo mal
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)  #puede ser falla de usuario o aplicacion
