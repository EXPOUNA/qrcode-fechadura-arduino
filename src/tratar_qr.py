import json

def decodificar_json(data):

    try:
        return json.loads(data)
    except json.JSONDecodeError:
        corrected_data = data.replace("'", '"')
        try:
            return json.loads(corrected_data)
        except json.JSONDecodeError as e:
            print(f"Erro ao corrigir JSON: {e}")
            print(f"Conteúdo bruto: {repr(data)}")
            return None

