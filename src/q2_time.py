from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Primero, se cargan todos los tweets desde el archivo.
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    # A continuación, se crea un único string que contiene el contenido de todos los tweets.
    single_string = "".join(json.loads(tweet)['content'] for tweet in tweets)
    
    # Usando emoji_list, se extraen todos los emojis del string completo.
    emojis = [emoji['emoji'] for emoji in emoji_list(single_string)]

    # Se cuentan los emojis y se retornan los 10 más frecuentes.
    return Counter(emojis).most_common(10)
