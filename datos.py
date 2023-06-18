import pandas as pd
import json
from pandas import json_normalize

def dic_toString(column):
    # Aplicar la función json.dumps a cada celda de la columna
    celda = column.apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)
    return celda

def list_toString(column):
    # Aplicar la función join a cada celda de la columna
    celda = column.apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    return celda

