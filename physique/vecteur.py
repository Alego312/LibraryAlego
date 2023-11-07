import math

class Vecteur:
    """
    init:
    vecteur: tuple # every dimension of the vector
    norme: float   # norme of the vector
    angle: float   # angle of the vector in degrees
    """
    def __init__(self, vecteur: tuple=None, norme: float=None, angle: float=None):
        if not vecteur and not norme and not angle:
            raise ValueError("Un vecteur doit être initialisé avec au moins un argument")
        if vecteur:
            self.vec = vecteur
            self.norme = math.sqrt(sum([i ** 2 for i in vecteur]))
            if len(vecteur) == 2:
                self.angle = math.atan(vecteur[1] / vecteur[0]) * 180 / math.pi
        else:
            self.vec = (norme * math.cos(angle * math.pi / 180), norme * math.sin(angle * math.pi / 180))
            self.norme = norme
            self.angle = angle

    # addition de vecteurs
    def __add__(self, other):
        if len(other.vec) != len(self.vec):
            raise ValueError("Les vecteurs doivent avoir la même dimension")
        else:
            j = ()
            for i in range(len(self.vec)):
                j += (self.vec[i] + other.vec[i],)
            return Vecteur(j)
    # soustraction de vecteurs
    def __sub__(self, other):
        if len(other.vec) != len(self.vec):
            raise ValueError("Les vecteurs doivent avoir la même dimension")
        else:
            j = ()
            for i in range(len(self.vec)):
                j += (self.vec[i] - other.vec[i],)
            return Vecteur(j)
    # multiplication sur un vecteur
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            j = ()
            for i in range(len(self.vec)):
                j += (self.vec[i] * other,)
            return Vecteur(j)
        elif isinstance(other, Vecteur):
            if len(self.vec) != 2:
                print("multiplication vectoriel a plus de ")
        else:
            raise ValueError("Le multiplicateur doit être un nombre ou un vecteur")
    # division sur un vecteur
    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            j = ()
            for i in range(len(self.vec)):
                j += (self.vec[i] / other,)
            return Vecteur(j)
        else:
            raise ValueError("Le diviseur doit être un nombre")


    #Get item
    def __getitem__(self, item):
        return self.vec[item]
    #Set item
    def __setitem__(self, key, value):
        j = ()
        for i in range(len(self.vec)):
            if i != key:
                j += (self.vec[i],)
            else:
                j += (value,)
        self.vec = j
    #del item
    def __delitem__(self, key):
        j = ()
        for i in range(len(self.vec)):
            if i != key:
                j += (self.vec[i],)
        self.vec = j
    #len
    def __len__(self):
        return len(self.vec)
    #print
    def __str__(self):
        return str(self.vec)
    #isinstance
    @staticmethod
    def isinstance(instance):
        return Vecteur == instance


a = Vecteur()
b = Vecteur((4, 1, 2))
print(a + b)