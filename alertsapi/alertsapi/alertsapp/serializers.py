from rest_framework import serializers 
from .models import Alertas

class AlertasSerializer(serializers.ModelSerializer):
	Post_id= serializers.CharField(max_length=1000, required=True)
	def create(self,validated_data):
		return Alertas.objects.create(text=validated_data.get('Post_id'))
		
	def update(self,instance,validated_data):
		instance.text = validated_data.get('Post_id',instance.text)
		instance.save()
		return instace 
		
	class Meta:
		model = Alertas
		fields = ('id','Empresa','Post_id','Post','Seguidores','Seguindo','Post_url','img','Likes','Comments','Periods','update_time')
	
