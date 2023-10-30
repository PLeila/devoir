import random
import pickle


lot_chans =0
chans = 5
esko=0

nbre_aleatoire=random.randint(10,140)
#print(nbre_aleatoire)
try:
    with open ('data.pickle', 'rb') as fiche:
        data=pickle.load(fiche)
except FileNotFoundError:
    data={}
epsedo=input("antre non itlizatew: ")
  
while ' ' in epsedo:  
    epsedo=input("non itlizatew pa sipoze gen espas eseye anko : ")
    if epsedo.islower() and not ' ':
        print("Nou kontan paske ou vin jwe ak nou {}".format(epsedo))

if epsedo in data:
    esko= data[epsedo]
    print("BOnjour! {} ansyen esko ou se {}".format(epsedo,esko ))
else:
    print("Bonjour! {}, byenvini nan jwet lawoulet la ak nou".format(epsedo))
    data[epsedo]=0
    
while True:
    while chans>0:
        
        nbre_chwazi=int(input("rantre yon nonb nan enteval 10 a 150: "))
        if (nbre_chwazi<10 or nbre_aleatoire>=140):
            print("nonb ou chwazi a pa nan enteval konsidere a: ")
            continue
        lot_chans+=1
        if nbre_chwazi<nbre_aleatoire:
            print("nonb ou chwazi a pi piti")
        elif(nbre_chwazi>nbre_aleatoire):
            print("nonb ou chwazi a pi gwo")
        else:
            nouvoEsko= 30*chans
            esko += nouvoEsko
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("Bravooo!! ou genyen {} nouvo esko ou se {}".format(epsedo, esko))
            data[epsedo]=esko
            with open ('data.pickle', 'wb') as fiche:
                pickle.dump(data, fiche)
                break
                
        chans -= 1
        print("hey! chans ou egal {}".format(chans))
        
    if chans==0:
        print("ou pedi Mr ou Mme {} , nonb ki te kache a se {} e esko ou rete {}".format(epsedo, nbre_aleatoire, esko))
        break
    
    kanpe=input("siw vle kanpe pwogram nan peze K: ")
    if kanpe.lower()=='k':
        chans==0
        print("mesi paske ou te chwazi jwe ak nou. bye bye")
        break
    else:
        chans=5
        print("ou genyen anko, {} chans".format(chans))
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        nbre_aleatoire=random.randint(10,140)