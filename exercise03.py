list(filter(lambda x: x!="a", list1))

list(map(lambda x: len(x),acciones))

list(map(lambda x: x+1, list(map(int, nums))))

dict(zip(list(map(lambda x: x, numbers)),list(map(lambda x: len(x), numbers))))

{n: list([n ** m  for m in range(2, m+1)]) for n in range(1,n+1)}

[[x for x in range(1,x+1)],[x*2 for x in range(1,x+1)],[x*3 for x in range(1,x+1)],[x*4 for x in range(1,x+1)],[x*5 for x in range(1,x+1)],[x*6 for x in range(1,x+1)],[x*7 for x in range(1,x+1)],[x*8 for x in range(1,x+1)],[x*9 for x in range(1,x+1)],[x*10 for x in range(1,x+1)]]

def F(c): return "o" in c
all([F(c) for c in C])

def pyramid(v):
    vlen = len(str(v))
    max_len = v * 4
    for i in range(v + 1):
        label = format(i, "02")
        print((f"{label} " * i).center(max_len))
    
pyramid(11)

class Alumnos:
    def __init__(self, materia_fav, materias_reprobadas, materias_exentas):
        self.materia_fav = materia_fav
        self.materias_reprobadas = materias_reprobadas
        self.materias_exentas = materias_exentas
        
    def costo_extras(self):
        print("El costo de tus extras será de:", self.materias_reprobadas*500)
        
    def mejores_materias(self):
        print("Eres muy bueno para", self.materias_exentas, "materias!")
        

def F(a): return True if 231%a==0 else False
all([F(a) for a in A])

def F(a,b): return 2**a - 1 == b
all([any([F(a,b) for a in A] for b in B)])
