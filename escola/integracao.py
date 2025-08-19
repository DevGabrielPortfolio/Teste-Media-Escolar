from escola.calcularMedia import calcular_media
from escola.VerificaMedia import verificar_media

def processar_notas(notas: list[float]) -> dict:
    """
    Processa uma lista de notas, calcula a média e verifica a aprovação.
    
    Parâmetros:
    notas (list[float]): Lista de notas a serem processadas.
    
    Retorna:
    dict: Dicionário contendo a média das notas e o status de aprovação.
    """
    try:
        # Calculando a média das notas
        media = calcular_media(notas)
        
        # Verificando o status de aprovação
        status = verificar_media(media)
        
        # Retornando os resultados
        return {
            "media": media,
            "status": status
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}