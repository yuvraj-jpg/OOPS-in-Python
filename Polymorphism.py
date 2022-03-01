# Polymorphism means the same function name (but different signature ) being used for different types
# Polymorphism with class

class India:
    def capital(self):
        print("New delhi is the capital of India ")
    def language(self):
        print("Hindi is the Most Widely Spoken language in India ")
    def type(self):
        print("India is developing country")
class Usa:
    def capital(self):
            print("Washington D.C is the capital of India ")
    def language(self):
        print("English is the Most Widely Spoken language in India ")
    def type(self):
        print("USA is developing country")
ob=India()
ob_usa=Usa()

ob.type()