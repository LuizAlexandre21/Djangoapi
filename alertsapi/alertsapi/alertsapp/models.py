from django.db import models

class Alertas(models.Model):
	id = models.AutoField(
	primary_key=True
	)
	
	Empresa = models.TextField(
	max_length = 100
	)
	
	Post_id = models.TextField(
	max_length = 100
	)
	
	Post = models.IntegerField()
	
	Seguidores = models.IntegerField()
	
	Seguindo = models.IntegerField()
	
	Post_url = models.TextField(
	max_length = 100
	)
	
	img = models.TextField(
	max_length =100
	)
	
	Likes = models.IntegerField()
	
	Comments = models.IntegerField()
	
	Periods = models.TextField(
	max_length =100
	)
	
	update_time = models.TextField(
	max_length =100
	)
	
	class Meta:
		db_table ='Alertas'
	
