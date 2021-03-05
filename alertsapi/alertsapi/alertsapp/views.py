from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin 
from .models import Alertas 
from .serializers import AlertasSerializer 
# Create your views here.

class AlertasListView(APIView, UpdateModelMixin,DestroyModelMixin ):

	def get(self,request, id=None):
		if id:
			try:
				queryset =Alertas.objects.get(id=id)
			except Alertas.DoesNotExist:
				return Response({'errors': 'This Alertas does not exist.'},status=400)
			
			read_serializer = AlertasSerializer(queryset)
		
		else:
			queryset = Alertas.objects.all()
			read_serializer = AlertasSerializer(queryset,many=True) 
		
		return Response(read_serializer.data)
		
	
	def post(self,request):
		create_serializer = AlertasSerializer(data=request.data)
		if create_serializer.is_valid():
			alertas_item_object = create_serializer.save()
			read_serializer =AlertasSerializer(alertas_item_object)
			return Response(read_serializer.data,status=201)
			
		return Response(create_serializer.errors,status=400)
	
	
	def put(self,request,id=None):
		try:
			alertas_item = Alertas.object.get(id=id)
		
		except Alertas.DoesNotExist:
			return Response({'errors':'This Alertas item does not exist.'},status=400)
		
		update_serializer - AlertasSerializer(alertas_item, data=request.data)
		
		if update_serializer.is_valid():
			alertas_item_object = update.serializer.save()
			
			read_serializer = AlertasSerializer(alertas_item_object)
			
			return Response(read_serializer.data,status=200)
		
		return Response(update_serializer.errors,status=400)
	
	
	def delete(self,request,id=None):
		try:
			alerta_item = Alerta.objects.get(id=id)
		except Alertas.DoesNotExist:
			return Response({'errors':"This Alertas item does not exist."},status=400)
			
		alertas_item.delete()
		
		return Response(status=204)
		
		
			
		
	
	
	
	
	
	
	
	
	
	
