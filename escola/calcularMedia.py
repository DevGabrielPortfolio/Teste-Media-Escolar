def calcular_media(numeros:list[float]) -> float:
    """
        Calcula a média de uma lista de notas.

        Parâmetros:
        notas (list[float]): Lista de notas a serem calculadas

        Retorna:
        float: A média das notas, arredondada para uma casa decimal
    """

    #   Verificando se a lista esta vazia
    if not numeros:

        raise ValueError("it is not allowed to send an empty list")
    
    for nota in numeros:
        # Verifica se a nota é uma string
        if isinstance(nota, str):
            
            raise TypeError("invalid note: texts are not allowed")

        # Verifica se a nota é maior que 10 ou menor que 0
        if(nota < 0 or nota > 10):
            raise ValueError("grades can be from 0 to 10")


    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade

    return round(media, 1)
