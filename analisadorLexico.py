import unicodedata
# from tabulate import tabulate

# Defina os estados do autômato como constantes
Q0 = 0
Q1 = 1
Q2 = 2
Q3 = 3
Q4 = 4
Q5 = 5
Q6 = 6
Q7 = 7
Q8 = 8
Q9 = 9
Q10 = 10
Q11 = 11
Q12 = 12
Q13 = 13
Q14 = 14
Q15 = 15
Q16 = 16
Q17 = 17
Q18 = 18
Q19 = 19
Q20 = 20
Q21 = 21
Q22 = 22
Q23 = 23
Q24 = 24
Q25 = 25
Q26 = 26
Q27 = 27
Q28 = 28
Q29 = 29
Q30 = 30
Q31 = 31
Q32 = 32
Q33 = 33
Q34 = 34
Q35 = 35
Q36 = 36
Q37 = 37
Q38 = 38
Q39 = 39
Q40 = 40
Q41 = 41
Q42 = 42
Q43 = 43
Q44 = 44
Q45 = 45
Q46 = 46
Q47 = 47
Q48 = 48


palavras_reservadas = ['fim_programa', 'programa', 'se', 'senao', 'entao', 'imprima', 'leia', 'enquanto']

def remover_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Função para identificar tokens
def identificar_token(lexema):
    
    lexema_sem_acentos = remover_acentos(lexema)
    
    if lexema in palavras_reservadas:
        return f"TK_{lexema.upper()}"
    
    if '.' in lexema:
        parts = lexema.split('.')
        if len(parts) == 2 and all(part.isalnum() for part in parts):
            return "TK_NUMERO"
    
    if 'e' in lexema:
        parts = lexema.split('e')
        if len(parts) == 2 and all(part.isalnum() for part in parts):
            return "TK_NUMERO"
    
    if 'e' in lexema:
        parts = lexema.split('e', 1)  # Limitando a divisão a uma vez
        if len(parts) == 2:
            num_part, exponent_part = parts
            if '.' in num_part:
                int_part, float_part = num_part.split('.', 1)
                if int_part.isalnum() and all(part.isalnum() for part in float_part) and (exponent_part.startswith('-') and exponent_part[1:].isalnum() or exponent_part.isalnum()):
                    return "TK_NUMERO"
    
    if lexema.isalnum() and lexema_sem_acentos.lower() not in map(lambda x: remover_acentos(x.lower()), palavras_reservadas):
        return "TK_NUMERO"
    
    if (
        lexema[0] in 'A-JRU' and
        lexema[1] == '$' and
        '.' in lexema and
        lexema.split('.')[1].isdigit() and
        len(lexema.split('.')[1]) == 2
    ):
        return "TK_MOEDA"
    
    if all(char in '-~+*/&!=>:<| ' for char in lexema):
        return "TK_OPERADOR"
    
    if all(char in ',() ' for char in lexema):
        return "TK_DELIMITADORES"
    
    if lexema.startswith('<') and lexema.endswith('>') and lexema[1:-1].isidentifier():
        return "TK_ID"
    
    if lexema.startswith('"') and lexema.endswith('"'):
        return "TK_CADEIA"
    
    if lexema.startswith("'''") and lexema.endswith("'''"):
        return "TK_COMENTARIO"
    
    if lexema.startswith("#") or " " in lexema:
        return "TK_COMENTARIO"
 
    if lexema == '\n' or lexema == '\t':
        return "TK_QUEBRADELINHA"
    
    return "ERRO!TK_DESCONHECIDO"


# Função principal do analisador léxico
def analisador_lexico(arquivo):
    estado_atual = Q0
    lexema = ""
    tokens = []
    linha = 1
    coluna = 0
    
    def exibir_erro(mensagem):
        print(f'ERRO: {mensagem}')
    
    erro = False  # Flag para indicar se ocorreu um erro

    char = arquivo.read(1)  # Leia um caractere por vez

    while char:
        if estado_atual == Q0:
            if 'A' <= char <= 'Z' or char.isdigit():
                estado_atual = Q41
                lexema = char
                char = arquivo.read(1)
                
            elif 'a' <= char <= 'z' or char == '_':
                estado_atual = Q39
                
            elif char == ' ':
                char = arquivo.read(1)
                continue

            elif char == '~':
                estado_atual = Q42

            elif char == '+':
                estado_atual = Q43

            elif char == '*':
                estado_atual = Q44

            elif char == '/':
                estado_atual = Q45

            elif char == '&':
                estado_atual = Q46

            elif char == '|':
                estado_atual = Q47

            elif char == '=':
                estado_atual = Q35

            elif char == '-':
                estado_atual = Q31

            elif char == ',':
                estado_atual = Q28
   
            elif char == '(':
                estado_atual = Q29
                lexema += char
                char = arquivo.read(1)
            
            elif char == ')':
                estado_atual = Q30
       
            elif char == '>':
                estado_atual = Q33

            elif char == '<':
                estado_atual = Q11

            elif char == ':':
                estado_atual = Q38

            elif char == '!':
                estado_atual = Q36

            elif char == '"':
                estado_atual = Q1

            elif char == "'":
                estado_atual = Q22

            elif char == "#":
                estado_atual = Q18

            elif char == "\n" or char == '\t':
                estado_atual = Q48

            
                
            
            else:
                # Caractere não reconhecido, trate o erro aqui
                pass


        # TRATAMENTO \n
        elif estado_atual == Q48:
            if char == "\n" or char == '\t':
                lexema += char
                char = arquivo.read(1)
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, repr('\n')))
                linha += 1 
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        #LEXEMA DAS PALAVRAS RESERVADAS 
        elif estado_atual == Q39:
            if ('a' <= char <= 'z') or char == '_':
                lexema += char
                char = arquivo.read(1)
                coluna
            elif char == '"' or char == 'ã':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q39
            else:
                estado_atual = Q40
        
        elif estado_atual == Q40:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        # LEXEMA DE CADEIA
        elif estado_atual == Q1:
            lexema += char
            char = arquivo.read(1)
            if char.isalpha() or char.isdigit():
                estado_atual = Q2
        elif estado_atual == Q2:
            lexema += char
            char = arquivo.read(1)
            if char == '"':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q3
        elif estado_atual == Q3:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
        

        # LEXEMA DE MOEDA OU DE NUMERO
        elif estado_atual == Q41:
            if char == '$':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q5
            elif char.isalnum():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q4

            elif char == '.':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q10
                    
        elif estado_atual == Q4:

            if char == 'e':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q14
                
            elif char.isalnum() and char != 'e' or char == '.':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q4
            else: 
                estado_atual = Q21
                
        elif estado_atual == Q21:
            # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                

        elif estado_atual == Q10:
            if char.isalnum() and char != 'e':
                lexema += char
                char = arquivo.read(1)

            elif char == 'e':
                estado_atual = Q14
                lexema += char
                char = arquivo.read(1)

            else:
                estado_atual = Q17
                
            
        elif estado_atual == Q17:
            # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
        
        elif estado_atual == Q14:
            if char == '-':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q15


            elif char.isalnum():
                estado_atual = Q4

        elif estado_atual == Q15:
            if char.isalnum():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q4
                
                

                



        
        
        # LEXEMA MOEDA
        elif estado_atual == Q5:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q6


        elif estado_atual == Q6:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
            elif char == '.':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q7

        elif estado_atual == Q7:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q8
            else:
                estado_atual = Q9

        elif estado_atual == Q8:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q9
            else:
                estado_atual = Q9
                
        elif estado_atual == Q9:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q9

            else:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)
                    tokens.append((linha, token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
   
         


        #LEXEMA DE OPERADORES 
        elif estado_atual == Q42:
            if char == '~':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
        
        elif estado_atual == Q43:
            if char == '+':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q44:
            if char == '*':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q45:
            if char == '/':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q46:
            if char == '&':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q47:
            if char == '|':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q35:
            if char == '=':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q31:
            if char == '-':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q33:
            if char != '=':
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

            elif char == '=':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q34

            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q38:
            if char == ':':
                lexema += char
                char = arquivo.read(1)
            elif char == '=':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q34

            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q36:
            if char == '!':
                lexema += char
                char = arquivo.read(1)
            elif char == '=':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q34


            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


        elif estado_atual == Q34:
            if char == '=': 
                print('s')

            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
            


        # Verifique o estado final para o último token


        
        




            

        #LEXEMAS DELIMITADORES
        elif estado_atual == Q28:
            if char == ',':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
        elif estado_atual == Q29:

                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, repr('(')))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


                

        elif estado_atual == Q30:
                lexema += char
                char = arquivo.read(1)
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                char = arquivo.read(1)
                tokens.append((linha, token, repr(')')))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                


        #LEXEMAS TK_ID
        elif estado_atual == Q11:
            if char == '<':
                lexema+=char
                char = arquivo.read(1)
                estado_atual = Q11

            if char == '=':
                lexema+=char
                char = arquivo.read(1)
                estado_atual = Q32

            elif char.isalpha() or char.isdigit():
                    estado_atual = Q12
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
        elif estado_atual == Q32:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        
        elif estado_atual == Q12:
            if char.isalpha() or char.isdigit():
                lexema += char
                char = arquivo.read(1)
            elif char == '>':
                    lexema += char
                    estado_atual = Q13
                    char = arquivo.read(1)
             
        elif estado_atual == Q13:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
            




        

        # COMENTARIO DE LINHA
        elif estado_atual == Q18:
            lexema += char
            char = arquivo.read(1)

            if char == '\n':
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
                
        elif estado_atual == Q20:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)
                    tokens.append((linha, token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
            



        elif estado_atual == Q24:
            if char.isdigit() or char.isalpha() or char == '-' or char == '.' or char == ' ':
                lexema += char
                char = arquivo.read(1)
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        #LEXEMAS COMENTARIO
        elif estado_atual == Q22:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q22
            else:
                estado_atual = Q16
                

        elif estado_atual == Q16:
            if char.isdigit() or char.isalpha() or char == '-' or char == '.' or char == ' ':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q16
            else:
                estado_atual = Q23


        elif estado_atual == Q23:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q23
            else :
                estado_atual = Q24

        elif estado_atual == Q24:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                tokens.append((linha, token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
 
        # Implemente outros estados e transições...
    return tokens    



# Função principal do analisador léxico
def analisador_lexico_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return analisador_lexico(arquivo)

token_counts = {}
total_tokens = 0

# Tamanho fixo de cada coluna
coluna_linha = 5
coluna_token = 20
coluna_lexema = 18

# Exemplo de uso
nome_arquivo = "texto.cic"  # Substitua pelo nome do seu arquivo
tokens = analisador_lexico_arquivo(nome_arquivo)
print("{:<{}} | {:<{}} | {:<{}}".format("Linha", coluna_linha, "Token", coluna_token, "Lexema", coluna_lexema))
print("-" * (coluna_linha + coluna_token + coluna_lexema + 3))
for linha, token, lexema in tokens:
    token_counts[token] = token_counts.get(token, 0) + 1
    print("{:<{}} | {:<{}} | {:<{}}".format(linha, coluna_linha, token, coluna_token, lexema, coluna_lexema))

print("=" * 100)
print("=" * 100)

print("{:<{}} | {:<{}}".format("Token", coluna_token, "Usos", 8))
print("-" * (coluna_token + 13))
for token, count in token_counts.items():
    print("{:<{}} | {:<{}}".format(token, coluna_token, count, 8))
    total_tokens += count
    
print("-" * (coluna_token + 13))
print("{:<{}} | {:<{}}".format("Total", coluna_token, total_tokens, 8))