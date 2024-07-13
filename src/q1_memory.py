from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Usamos defaultdict para facilitar el conteo de tweets por usuario y fecha.
    dates_dict = defaultdict(lambda: defaultdict(int))
    
    with open(file_path, 'r') as f:
        # Procesamos el archivo línea por línea para optimizar el uso de memoria.
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            
            # Aumentamos el contador de tweets de un usuario para esa fecha.
            dates_dict[tweet_date][username] += 1
    
    # Ordenamos las fechas según la cantidad total de tweets para identificar las más activas.
    top_dates = sorted(dates_dict.keys(), key=lambda x: sum(dates_dict[x].values()), reverse=True)[:10]
    
    # Obtenemos el usuario que más tweets ha realizado en cada una de las fechas seleccionadas.
    top_users = [max(dates_dict[date], key=dates_dict[date].get) for date in top_dates]

    # Convertimos las fechas a objetos datetime.date.
    top_dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in top_dates]
    
    # Retornamos una lista de tuplas con las fechas y los usuarios destacados.
    return list(zip(top_dates, top_users))
