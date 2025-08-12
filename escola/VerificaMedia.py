def verificar_media(nota: float) -> str:
    if isinstance(nota, str):  # Verifica se a nota é uma string
        raise TypeError("É necessário que seja um número")
    
    if nota < 0 or nota > 10: # Verifica se a nota esta no intervalo correto
        raise ValueError("Nota deve estar entre 0 e 10")
    
    if 0 <= nota <= 5: # Verifica se o aluno esta reprovado
        return "Reprovado"
    
    if 5 < nota <= 7: # Verifica se o aluno esta de recuperação
        return "Recuperação"
    
    if 7 < nota <= 10: # Verifica se o aluno esta aprovado
        return "Aprovado"
