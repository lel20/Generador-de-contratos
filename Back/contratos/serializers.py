from rest_framework import serializers
from models import plantillaContrato, contratoGenerado

class plantillaContratoSerilizer(serializers.ModelSerializer):
    model=plantillaContrato
    class Meta:
        fields=['id','titulo','descripcion','contenido','categoria','fecha_creacion']
class contratoGeneradoSerializer(serializers.ModelSerializer):
    model=contratoGenerado
    class Meta:
        fields=['id','id_usuario','id_plantilla','datos_completos','texto_completo','fecha_creacion','descarga']
         