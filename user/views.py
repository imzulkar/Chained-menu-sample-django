from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from user import models, serializers, apipermissions
from rest_framework import generics, status, response

from user.models import Project


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    JWT Custom Token Claims Serializer
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.full_name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """
    JWT Custom Token Claims View
    """
    serializer_class = MyTokenObtainPairSerializer


class NewUserView(generics.ListCreateAPIView):
    """
    New User Create View
    """
    serializer_class = serializers.NewUserSerializer
    queryset = models.User.objects.all()

    # permission_classes = [apipermissions.IsSuperUser]

    def create(self, request, *args, **kwargs):
        user = request.data
        ser = self.serializer_class(data=user)
        ser.is_valid(raise_exception=True)
        new_user = ser.save()
        user_data = ser.data
        tokens = RefreshToken.for_user(new_user)
        refresh = str(tokens)
        access = str(tokens.access_token)

        return response.Response({'user_data': user_data, 'refresh_token': refresh, 'access_token': access},
                                 status=status.HTTP_201_CREATED)


@login_required
def get_phases(request):
    project = request.POST.get('project')
    phases = {}
    try:
        if project:
            prophases = Project.objects.get(pk=int(project)).phase
            phases = {pp.phase.title: pp.pk for pp in prophases}
    except:
        pass
    return JsonResponse(data=phases, safe=False)



@login_required
def provinsi_list(request):
    provinsi = models.Provinsi.objects.all()
    return JsonResponse({'data': [{'id': p.id, 'name': p.name} for p in provinsi]})


@login_required
def kabupaten_list(request, provinsi_id):
    kabupaten = models.Kabupaten.objects.filter(provinsi=provinsi_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in kabupaten]})


@login_required
def kecamatan_list(request, kabupaten_id):
    kecamatan = models.Kecamatan.objects.filter(kabupaten_id=kabupaten_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in kecamatan]})


@login_required
def kelurahan_list(request, kecamatan_id):
    kelurahan = models.Kelurahan.objects.filter(kecamatan_id=kecamatan_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in kelurahan]})