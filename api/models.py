from django.db import models

class generos(models.Model):
    generos_id =models.AutoField(primary_key=True)
    tipo_generos= models.CharField(max_length=255)
    
    class Meta:
        db_table= "generos"
        
class usuarios (models.Model):
    usuarios_id= models.AutoField(primary_key=True)
    nombre_completo= models.CharField(max_length=255)
    fk_generos= models.ForeignKey(generos, on_delete=models.CASCADE)
    
    class Meta:
        db_table= "usuarios"        
# Create your models here.