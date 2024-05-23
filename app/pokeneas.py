import random

POKENEAS = [
    {"id": 125, "nombre": "Electabuzz", "altura": 1.1, "habilidad": "Elect. Estatica", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/125.png", "frase_filosofica": "La vida es como una caja de chocolates"    },
    {"id": 110, "nombre": "Weezing", "altura": 1.2, "habilidad": "Levitacion, Gas reactivo", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/110.png", "frase_filosofica": "Mejor afuera que adentro"    },  
    {"id": 212, "nombre": "Scizor", "altura": 1.8, "habilidad": "Enjambre", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/212.png", "frase_filosofica": "Como dijo andrea, suerte ..."    },
    {"id": 13, "nombre": "Weedle ", "altura": 0.3, "habilidad": "Polvo Escudo", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/013.png", "frase_filosofica": "Aqui las tengo para que me las ..."    },
    {"id": 31, "nombre": "Nidoqueen ", "altura": 1.3, "habilidad": "Punto Tóxico", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/031.png", "frase_filosofica": "Con quien peleo que solo muñecos veo"    },
    {"id": 313, "nombre": "Volbeat  ", "altura": 0.7, "habilidad": "Enjambre, Iluminaciòn", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/313.png", "frase_filosofica": "Me comunico con mi cola"    },
    {"id": 186, "nombre": "Politoed  ", "altura": 1.1, "habilidad": "Absorbe agua", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/186.png", "frase_filosofica": "Se descuidan y me les bebo todo"    },
    {"id": 865, "nombre": "Sirfetch’d ", "altura": 0.8, "habilidad": "Impasible", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/865.png", "frase_filosofica": "Que pereza el puerco ome"    },
    {"id": 899, "nombre": "Wyrdeer", "altura": 1.8, "habilidad": "Intimidacion y cacheo", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/899.png", "frase_filosofica": "Si, soy cachon y que!"    },
    {"id":512 , "nombre": " Simisage ", "altura": 1.1, "habilidad": "Gula", "imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/512.png", "frase_filosofica": "Todo si, nada no y como fue"    },
]           

def obtener_pokenea_aleatorio():
    return random.choice(POKENEAS)
