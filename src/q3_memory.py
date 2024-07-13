from typing import List, Tuple
import json
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Se inicializa el objeto Counter para contar los usernames.
    users_counter = Counter()
    
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            # Verificamos si se ha llegado al final del archivo.
            if not line:
                break
            # Obtenemos la lista de users dentro de mentionedUsers; si es None, se omite la línea.
            mentioned_users = json.loads(line)['mentionedUsers']
            if mentioned_users is None:
                continue
            # Extraemos los usernames y actualizamos el contador.
            usernames = [user['username'] for user in mentioned_users]
            users_counter.update(usernames)

    # Retornamos los 10 usernames más mencionados.
    return users_counter.most_common(10)
