import json


# ABRIR/GUARDAR .json
def Abrir_DataSet(file_name: str) -> list:
    file: list = open(file_name, 'r', encoding = 'utf8')
    DATA_SET: list = json.load(file)
    return DATA_SET


def Guardar_DataSet(file_name: str, dataSet: list) -> None:
    file = open(file_name, 'w', encoding = 'utf8')
    json.dump(dataSet, file, ensure_ascii = False)
    file.close()
