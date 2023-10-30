import random
import pickle

# Inisyalize varyab "scores" kom yon tach vid nan komansman an
scores = {}

# Fonksyon pou tcheke si yon epsedo valab (pa gen espas, ak nan piti)
def epsedo_valab(epsedo):
    return epsedo.islower() and ' ' not in epsedo

# Komanse jwet la
while True:
    print("Byenveni nan jwet Lawoulet!\nchwazi yon nimewo ant 0 ak 100")

    # Antre limit enferye nan enteval la
    while True:
        limit_enferye = int(input("Antre limit enferye nan enteval la : "))
        if 0 <= limit_enferye <= 100:
            break
        else:
            print("Tanpri antre yon nonm ant 0 ak 100.")

    # Antre limit siperye nan enteval la
    while True:
        limit_siperye = int(input("Antre limit siperye nan enteval la : "))
        if 0 <= limit_siperye <= 100:
            break
        else:
            print("Tanpri antre yon nonm ant 0 ak 100.")

    nimewo_sekre = random.randint(limit_enferye, limit_siperye)
    chans = 5  # Ou ka chanje kantite chans yo si ou vle

    epsedo = input("Antre yon epsedo (pa gen espas) : ").lower()

    if not epsedo_valab(epsedo):
        print("Epsedo pa valab. Asire ou pa gen espas nan li")
        continue
    
    