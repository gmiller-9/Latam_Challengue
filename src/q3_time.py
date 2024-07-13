from typing import List, Tuple
from collections import Counter
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Se extraen las listas de usuarios mencionados en cada tweet
    with open(file_path, 'r') as f:
        data = [json.loads(line)['mentionedUsers'] for line in f]

    # Se obtiene el username de cada usuario en las listas de mentionedUsers, ignorando las listas vacías.
    usernames = [user['username'] for obj in data if obj is not None for user in obj]

    # Se retornan los 10 usernames más frecuentes utilizando Counter.
    return Counter(usernames).most_common(10)
