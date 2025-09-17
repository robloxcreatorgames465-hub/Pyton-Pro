# Pyton-Pro
# My primer projecto de pyton pro
for i in range(5):
    
    meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Buen juego en ingles",
            "EZ": "Facil en ingles, se usa como burla",
            "BRAINROT":"Objeto sin sentido generado por IA"
            
            }
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("palabra no encontrada")
