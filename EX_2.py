def count_letter_a(text):
    count = text.lower().count('a')
    print(f"A letra 'a' aparece {count} vezes na string.")

# String de teste
string_teste = "Exemplo de Análise de presença da letra A"
count_letter_a(string_teste)