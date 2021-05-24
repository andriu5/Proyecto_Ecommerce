from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PaisesManager(models.Manager):
    def pais_validator(self,postData):
        pais_to_create=Paises.objects.filter(nombre=postData['pais'])
        errors={}
        if len(postData['nombre'])<2:
            errors['nombre_pais']="El nombre del país debe tener a lo menos dos caracteres."
        if not postData['nombre'].isalpha():
            errors['alpha_pais']="El nombre del país debe contener solo letras."
        if len(pais_to_create)>0:
            errors['país'] = "El país ya fue registrado."
        # if datetime.strptime(postData['birth_date'],'%Y-%m-%d')>=datetime.now()-timedelta(days=4745):
        #     errors['birth_date']="Debe tener a lo menos 13 años."
        return errors        

class RegionesManager(models.Manager):
    def region_validator(self,postData):
        region_to_create=Regiones.objects.filter(nombre=postData['region'])
        errors={}
        if len(postData['nombre'])<2:
            errors['nombre_region']="El nombre de la región debe tener a lo menos dos caracteres."
        if not postData['nombre'].isalpha():
            errors['alpha_region']="El nombre de la región debe contener solo letras."
        if len(region_to_create)>0:
            errors['region'] = "La región ya fue registrado."
        # if datetime.strptime(postData['birth_date'],'%Y-%m-%d')>=datetime.now()-timedelta(days=4745):
        #     errors['birth_date']="Debe tener a lo menos 13 años."
        return errors

class CiudadesManager(models.Manager):
    def ciudad_validator(self,postData):
        ciudad_to_create=Ciudades.objects.filter(nombre=postData['ciudad'])
        errors={}
        if len(postData['nombre'])<2:
            errors['nombre_ciudad']="El nombre de la ciudad debe tener a lo menos dos caracteres."
        if not postData['nombre'].isalpha():
            errors['alpha_ciudad']="El nombre de la ciudad debe contener solo letras."
        if len(ciudad_to_create)>0:
            errors['ciudad'] = "La ciudad ya fue registrado."
        # if datetime.strptime(postData['birth_date'],'%Y-%m-%d')>=datetime.now()-timedelta(days=4745):
        #     errors['birth_date']="Debe tener a lo menos 13 años."
        return errors

class DireccionesManager(models.Manager):
    def direccon_validator(self,postData):
        errors={}
        if not(postData['tipo'])=='P' or not(postData['tipo']=='C'):
            errors['tipo_direccion']="El tipo de dirección no es correcto. Utilice sólo el formulario para seleccionar este valor."
        if not postData['tipo'].isalpha():
            errors['tipo_direccion_alpha']="El tipo de dirección debe contener solo letras."
        if len(postData['calle'])<4:
            errors['largo_calle']="El largo del nombre de la calle debe tener a lo menos 4 caracteres."
        if len(postData['numero'])<2:
            errors['largo_numero']="El largo del numero de la dirección debe tener a lo menos 2 caracteres."
        # if datetime.strptime(postData['birth_date'],'%Y-%m-%d')>=datetime.now()-timedelta(days=4745):
        #     errors['birth_date']="Debe tener a lo menos 13 años."
        return errors

class Ordenes(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    # codigofecha=models.IntegerField()
    total=models.IntegerField() #debe ser actualizado por la aplicación, nunca en forma directa.
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    cliente=models.ForeignKey(
        Usuarios,
        related_name="clientes",
        on_delete=models.CASCADE
    )
    estado=models.ForeignKey(
        Estados,
        related_name='ordenes',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-fecha']
        indexes = [
            models.Index(fields=['fecha']),
            models.Index(fields=['codigofecha'])
        ]

class Productos(models.Model):
    # marca=models.CharField(max_length=100)
    # modelo=models.CharField(max_length=100)
    # merma=models.BooleanField(default=False)
    # precio_costo=models.IntegerField(validators = [
    #     MinValueValidator(0, message="No pueden ingresarse valores negativos")
    # ])
    cantidad_vendida=models.PositiveIntegerField(default=0)
    precio_venta=models.PositiveIntegerField(default=0)
    CATEGORIA = (
        ('1', 'COMPUTACION'),
        ('2', 'VESTUARIO'),
        ('3', 'MENAJE'),
        ('4', 'FRUTAS Y VERDURAS'),
    )
    categoria=models.CharField(max_length=1,choices=CATEGORIA,default='1')
    inventario=models.PositiveIntegerField(default=0)
    descripcion=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    # class Meta:
    #     unique_together = (("numero_serie", "marca", "modelo"),)
    

class Paises(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
    #     unique_together = (("nombre", "apellido"),)
        ordering = ['nombre']

class Regiones(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    pais=models.ForeignKey(
        Paises,
        related_name='regiones',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['nombre']

class Ciudades(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    region=models.ForeignKey(
        Regiones,
        related_name="ciudades",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['nombre']

class Direcciones(models.Model):
    TIPO = (
        ('P', 'PARTICULAR'),
        ('C', 'COMERCIAL'),
    )

    tipo=models.CharField(max_length=1,choices=TIPO,default='P')
    calle=models.CharField(max_length=50)
    numero=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    usuario=models.ForeignKey(
        Usuarios,
        related_name="direcciones",
        on_delete=models.CASCADE
    )
    ciudad=models.ForeignKey(
        Ciudades,
        related_name="ciudades",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['calle']