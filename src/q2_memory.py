from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from emoji import emoji_list

def q2_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Este contador se actualizará con cada lista de emojis encontrada en las líneas.
    emoji_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet_content = json.loads(line)['content']
            
            # Se extraen los emojis del contenido del tweet
            tweet_emojis = [emoji['emoji'] for emoji in emoji_list(tweet_content)]
            
            # Se suman los emojis encontrados al contador total.
            emoji_counter.update(tweet_emojis)
    
    # Se retornan los 10 emojis más frecuentes en el archivo.
    return emoji_counter.most_common(10)
