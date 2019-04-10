from django.db import models

# Create your models here.


"""PowerLog Model to log consumption """ 
class PowerLog(models.Model): 
	power = models.DecimalField(max_digits=10, decimal_places=2)
	duration = models.DecimalField(max_digits=10, decimal_places=2)
	pv = models.DecimalField(max_digits=10, decimal_places=4)
	registered_at = models.DateTimeField(auto_now_add=True)

	def __str__(self): 
		return str(self.registered_at)




