from django.core.exceptions import ValidationError
import sys
from itertools import cycle

def validarRut(rut):
	rut = rut.upper();
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]
 
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
 
	if str(res) == dv:
		return True
	elif dv=="K" and res==10:
		return True
	else:
		raise ValidationError("The Password is too long. It's length must be less than 10") 
 
 

def check_pass_size(value):
    if len(value) > 3:
        raise ValidationError("The Password is too long. It's length must be less than 10") 