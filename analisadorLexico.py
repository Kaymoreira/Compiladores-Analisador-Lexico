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

def is_valid_hexadecimal(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def is_valid_scientific_notation(s):
    parts = s.split('e')
    if len(parts) == 2 and all(part.replace('-', '').isdigit() for part in parts):
        return True
    return False

# Função para identificar tokens
def identificar_token(lexema):
    if lexema in palavras_reservadas:
        return f"TK_{lexema.upper()}"
    
    if '.' in lexema:
        parts = lexema.split('.')
        if len(parts) == 2 and all(part.isalnum() for part in parts):
            return "TK_NUMERO"
    
    if 'e' in lexema and is_valid_scientific_notation(lexema):
        return "TK_NUMERO"

    if lexema.isdigit() or (lexema.startswith('-') and lexema[1:].isdigit()):
        return "TK_NUMERO"
    
    
    if lexema.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'U', 'R',)) and lexema[1] == '$' and lexema[2:].replace('.', '').isdigit():
        return "TK_MOEDA"
    
    if all(char in '-~+*/&!=>:| ' for char in lexema):
        return "TK_OPERADOR"
    
    if all(char in ', ' for char in lexema):
        return "TK_DELIMITADORES"
    
    if lexema.startswith('<') and lexema.endswith('>') and lexema[1:-1].isidentifier():
        return "TK_ID"
    
    if lexema.startswith('"') and lexema.endswith('"'):
        return "TK_CADEIA"
    
    if lexema.startswith("'''") and lexema.endswith("'''"):
        return "TK_COMENTARIO"
    
    if lexema.startswith("#") and " " in lexema:
        return "TK_COMENTARIO"
 
    if lexema == '\n' or lexema == '\t':
        return "TK_QUEBRADELINHA"
    
    return "TK_DESCONHECIDO"


# Função principal do analisador léxico
def analisador_lexico(arquivo):
    estado_atual = Q0
    lexema = ""
    tokens = []
    
    def exibir_erro(mensagem):
        print(f'ERRO: {mensagem}')
    
    erro = False  # Flag para indicar se ocorreu um erro

    char = arquivo.read(1)  # Leia um caractere por vez

    while char:
        if estado_atual == Q0:
            if 'A' <= char <= 'Z' or char.isdigit():
                estado_atual = Q41

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
                print(lexema)
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, repr('\n')))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        #LEXEMA DAS PALAVRAS RESERVADAS 
        elif estado_atual == Q39:
            if ('a' <= char <= 'z') or char == '_':
                lexema += char
                char = arquivo.read(1)
                print(lexema)
            else:
                estado_atual = Q40
        
        elif estado_atual == Q40:
                estado_atual = Q0
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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

                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)
                    char = arquivo.read(1)
                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
            
        
        elif estado_atual == Q14:
            if char == '-':
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q15


            elif char.isalnum():
                lexema += char
                char = arquivo.read(1)

            else:
                estado_atual = Q16
                    
        elif estado_atual == Q15:
            if char.isalnum():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q16
                
                

                
        elif estado_atual == Q16:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


        
        
        # LEXEMA MOEDA
        elif estado_atual == Q5:
            if char == ' ' or char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q6
            else:
                    exibir_erro(f"Erro no estado Q5. Esperado espaço ou dígito, encontrado: '{char}'")
                    lexema = ""
                    estado_atual = Q0

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

        elif estado_atual == Q8:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q9

        elif estado_atual == Q9:
            if char.isdigit():
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q9

            else:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)

                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    elif token == "TK_DESCONHECIDO":
                        print(f"Erro no estado Q9. Caractere inesperado: {char} no token {token}, lexema: {lexema}")
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q33:
            if char != '=':
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)

                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
            elif char != '=':
                print("DEU ERRO POIS SO TINHA O CARACTER : E ELE NAO EXISTE")
                estado_atual = Q0
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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

            elif char != '=':
                print("DEU ERRO POIS SO TINHA O CARACTER ! E ELE NAO EXISTE")
                estado_atual = Q0
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


        elif estado_atual == Q34:
            if char == '=': 
                print('s')

            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
        elif estado_atual == Q29:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                char = arquivo.read(1)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, repr('(')))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


                

        elif estado_atual == Q30:

                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                char = arquivo.read(1)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, repr(')')))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                


        #LEXEMAS TK_ID
        elif estado_atual == Q11:
            if char == '<':
                lexema+=char
                char = arquivo.read(1)

            if char == '=':
                lexema+=char
                estado_atual = Q32

            if char != '=' and not char.isalpha():
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)

                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
            elif char.isalpha():
                    estado_atual = Q12
        
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
                char = arquivo.read(1)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
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

                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
                
        elif estado_atual == Q20:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)
                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
            



        elif estado_atual == Q24:
            if char.isdigit() or char.isalpha() or char == '-' or char == '.' or char == ' ':
                lexema += char
                char = arquivo.read(1)

            elif char.isspace():
                continue
            else :
                lexema+=char
                estado_atual = Q25

        elif estado_atual == Q25:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q26


        elif estado_atual == Q26:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q27



        elif estado_atual == Q27:
            if char == "'":
                lexema += char
                char = arquivo.read(1)

            else:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)
                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0

        #LEXEMAS COMENTARIO
        elif estado_atual == Q22:
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q23
                

        elif estado_atual == Q23:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q24



        elif estado_atual == Q24:
            if char.isdigit() or char.isalpha() or char == '-' or char == '.' or char == ' ':
                lexema += char
                char = arquivo.read(1)

            elif char.isspace():
                continue
            else :
                lexema+=char
                estado_atual = Q25

        elif estado_atual == Q25:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q26


        elif estado_atual == Q26:
            if char == "'":
                lexema += char
                char = arquivo.read(1)
                estado_atual = Q27


        elif estado_atual == Q27:
            if char == "'":
                lexema += char
                char = arquivo.read(1)

            else:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)

                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
                    
 
        # Implemente outros estados e transições...
    return tokens    



# Função principal do analisador léxico
def analisador_lexico_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return analisador_lexico(arquivo)

# Tamanho fixo de cada coluna
coluna_token = 18
coluna_lexema = 18

# Exemplo de uso
nome_arquivo = "texto.cic"  # Substitua pelo nome do seu arquivo
tokens = analisador_lexico_arquivo(nome_arquivo)
print("{:<{}} | {:<{}}".format("Token", coluna_token, "Lexema", coluna_lexema))
print("-" * (coluna_token + coluna_lexema + 3))
for token, lexema in tokens:
    print("{:<{}} | {:<{}}".format(token, coluna_token, lexema, coluna_lexema))
