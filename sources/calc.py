<<<<<<< HEAD
"""
La librairie calc pvvermet de faire les opérations basiques de calcul entre deux entiers.
"""

def add(arg1,arg2):
    try:
        return int(arg1)+int(arg2)
    except ValueError: 
        print("Vous devez entrer un entier.") 

def sous(arg1,arg2):
    try:
        return int(arg1)-int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 


def mult(arg1,arg2):
    try:
        return int(arg1)*int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 

def div(arg1,arg2):
    try:
        return int(arg1)/int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 
    except ZeroDivisionError:
        print("Vous divisez par 0.")

def modulo(arg1,arg2):
    try:
        return int(arg1)%int(arg2)
    except ValueError:
        print("Un des arguments n'est pas un entier")    

def ope(operateur,arg1,arg2):   
    if operateur=='+':
        return add(arg1,arg2)        
    elif operateur=="%":
        return modulo(arg1,arg2)
    elif operateur=="-":
        return sous(arg1,arg2)
    elif operateur=="x":
        return mult(arg1,arg2)
    elif operateur=="/":
        return div(arg1,arg2)
    else:
        print("L'opérateur {} n'est pas reconnu.".format(operateur))
=======
print("Boxxnjour Jvb Saoussen.\n")
>>>>>>> c89db7ad233b859c3f2ed8141be3426a8afc2ec5
