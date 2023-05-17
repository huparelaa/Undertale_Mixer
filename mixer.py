from pydub import AudioSegment
pistas = {"Megalovania":"Pistas//Megalovania.mp3",
          "Hopes and dreams":"Pistas//Hopes_and_dreams.mp3",
          "Asgore":"Pistas//Asgore.mp3",
          "Muffet":"Pistas//Muffet.mp3",
          "Papyrus":"Pistas//Papyrus.mp3",
          "???":"Pistas//unknown.mp3",
          "Death by glamour": "Pistas//Death_by_glamour.mp3"
          }
def getCanciones():

    return pistas

def mix(cancion1,cancion2):
    pista1 = AudioSegment.from_file(pistas[cancion1], format="mp3")
    pista2 = AudioSegment.from_file(pistas[cancion2], format="mp3")
    # Mezclar las pistas
    if(len(pista2)>len(pista1)):
        mezcla = pista2.overlay(pista1)
    else:
        mezcla = pista1.overlay(pista2)

    return mezcla