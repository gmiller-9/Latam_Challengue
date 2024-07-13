from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Primero, almacenamos las fechas y usernames en una lista para poder contarlos posteriormente.
    with open(file_path, 'r') as f:
        data = [[json.loads(line)['date'].split('T')[0], json.loads(line)['user']['username']] for line in f]

    # Usamos Counter para obtener las 10 fechas más comunes de todos los tweets.
    most_common_dates = Counter([d[0] for d in data]).most_common(10)

    # De manera similar, encontramos el usuario que más ha tweetiado en cada una de las fechas más comunes.
    most_common_users = [Counter([d[1] for d in data if d[0] == date[0]]).most_common(1)[0][0] for date in most_common_dates]

    # Finalmente, utilizamos zip para agrupar las listas, convirtiendo la fecha a formato datetime.date().
    return list(zip([datetime.strptime(date[0], "%Y-%m-%d").date() for date in most_common_dates], most_common_users))
