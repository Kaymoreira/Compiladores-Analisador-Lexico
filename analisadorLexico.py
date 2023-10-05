import re

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

palavras_reservadas = ['fim_programa', 'programa', 'se', 'senao', 'entao', 'imprima', 'leia', 'enquanto']

# Função para identificar tokens
def identificar_token(lexema):
    if lexema in palavras_reservadas:
        return f"TK_{lexema.upper()}"
    elif re.match(r'^([A-F0-9]+(\.[A-F0-9]+)?([eE][\+\-]?[A-F0-9]+)?)$', lexema):
        return "TK_NUMERO"
    elif re.match(r'^[A-Z]\$\d+(\.\d{2})?$', lexema):
        return "TK_MOEDA"
    elif re.match(r'^[-~+*/&!=>:| ]+$', lexema):
        return "TK_OPERADOR"
    elif re.match(r'^[(, )\s]+$', lexema):
        return "TK_DELIMITADORES"
    elif re.match(r'<([a-z][a-z0-9]*)>', lexema) or re.match(r"^[<=]+$", lexema):
        return "TK_ID"
    elif re.match(r'^"[a-zA-Z0-9 .\s]*"$', lexema):
        return "TK_CADEIA"
    elif re.match(r"^'''[a-zA-Z0-9\s\-\.]+'''$", lexema) or re.match(r"^#.*(\n)?$", lexema):
        return "TK_COMENTARIO"
    else:
        return "TK_DESCONHECIDO"

# Função principal do analisador léxico
def analisador_lexico(arquivo):
    estado_atual = Q0
    lexema = ""
    tokens = []
    char_anterior = ''
    
    def exibir_erro(mensagem):
        print(f'ERRO: {mensagem}')
    
    erro = False  # Flag para indicar se ocorreu um erro

    for char in arquivo.read():
        if estado_atual == Q0:
            if char.isalpha() or char.isdigit() or char.isalnum():
                estado_atual = Q41
                lexema = char  
            elif char == '~':
                estado_atual = Q42
                lexema = char
            elif char == '+':
                estado_atual = Q43
                lexema = char
            elif char == '*':
                estado_atual = Q44
                lexema = char
            elif char == '/':
                estado_atual = Q45
                lexema = char
            elif char == '&':
                estado_atual = Q46
                lexema = char
            elif char == '|':
                estado_atual = Q47
                lexema = char
            elif char == '=':
                estado_atual = Q35
                lexema = char
            elif char == '-':
                estado_atual = Q31
                lexema = char
            elif char == ',':
                estado_atual = Q28
                lexema = char
            elif char == '(':
                estado_atual = Q29
                lexema = char
            elif char == ')':
                estado_atual = Q30
                lexema = char
            elif char == '>':
                estado_atual = Q33
                lexema = char
            elif char == '<':
                estado_atual = Q11
                lexema = char
            elif char == ':':
                estado_atual = Q38
                lexema = char
            elif char == '!':
                estado_atual = Q36
                lexema = char
            elif char == '"':
                estado_atual = Q1
                lexema = char
            elif char == "'":
                estado_atual = Q22
                lexema = char
            elif char == "#":
                estado_atual = Q18
                lexema = char
            
                
            elif char.isspace():
                continue
            else:
                # Caractere não reconhecido, trate o erro aqui
                pass

        # LEXEMA DE CADEIA
        elif estado_atual == Q1:
            lexema += char
            if char.isalpha() or char.isdigit():
                estado_atual = Q2
        elif estado_atual == Q2:
            lexema += char
            if char == '"':
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
                estado_atual = Q5
            elif char.isalnum():
                lexema += char
                estado_atual = Q4

            elif char == '.':
                lexema += char
                estado_atual = Q10

                    
        elif estado_atual == Q4:

            if char == 'e':
                lexema += char
                estado_atual = Q14
                
            elif char.isalnum() and char != 'e' or char == '.':
                lexema += char
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

            elif char == 'e':
                estado_atual = Q14
                lexema += char

            else:

                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)

                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
            
        
        elif estado_atual == Q14:
            if char == '-':
                lexema += char
                estado_atual = Q15


            elif char.isalnum():
                lexema += char

            else:
                estado_atual = Q16
                    
        elif estado_atual == Q15:
            if char.isalnum():
                lexema += char
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
                estado_atual = Q6
            else:
                    exibir_erro(f"Erro no estado Q5. Esperado espaço ou dígito, encontrado: '{char}'")
                    lexema = ""
                    estado_atual = Q0

        elif estado_atual == Q6:
            if char.isdigit():
                lexema += char
            elif char == '.':
                lexema += char
                estado_atual = Q7

        elif estado_atual == Q7:
            if char.isdigit():
                lexema += char
                estado_atual = Q8

        elif estado_atual == Q8:
            if char.isdigit():
                lexema += char
                estado_atual = Q9

        elif estado_atual == Q9:
            if char.isdigit():
                lexema += char
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
            elif char == '=':
                lexema += char
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
            elif char == '=':
                lexema += char
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

                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


                

        elif estado_atual == Q30:

                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)

                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                


        #LEXEMAS TK_ID
        elif estado_atual == Q11:
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
                    lexema += char
                    estado_atual = Q12
        
        elif estado_atual == Q12:
            lexema += char

            if char == '>':
                estado_atual = Q13
            elif not char.isdigit() and not char.isalpha() and char != '>':
                print(f"Erro no estado Q12. por falta de '>' para fechamento no token TK_ID, lexema: {lexema}")
                lexema = ""
                estado_atual = Q0
            
             
        elif estado_atual == Q13:

                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)

                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
            




        

        # COMENTARIO DE LINHA
        elif estado_atual == Q18:

            if char.isalpha() or char.isdigit() or char == ' ':
                lexema += char

            elif char == '\n':
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

            elif char.isspace():
                continue
            else :
                lexema+=char
                estado_atual = Q25

        elif estado_atual == Q25:
            if char == "'":
                lexema += char
                estado_atual = Q26


        elif estado_atual == Q26:
            if char == "'":
                lexema += char
                estado_atual = Q27



        elif estado_atual == Q27:
            if char == "'":
                lexema += char

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
                estado_atual = Q23
                

        elif estado_atual == Q23:
            if char == "'":
                lexema += char
                estado_atual = Q24



        elif estado_atual == Q24:
            if char.isdigit() or char.isalpha() or char == '-' or char == '.' or char == ' ':
                lexema += char

            elif char.isspace():
                continue
            else :
                lexema+=char
                estado_atual = Q25

        elif estado_atual == Q25:
            if char == "'":
                lexema += char
                estado_atual = Q26


        elif estado_atual == Q26:
            if char == "'":
                lexema += char
                estado_atual = Q27


        elif estado_atual == Q27:
            if char == "'":
                lexema += char

            else:
                    # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                    token = identificar_token(lexema)

                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
                    
        
      


    if erro:
        lexema = ""
        estado_atual = Q0

 
        # Implemente outros estados e transições...



    return tokens

# Função principal do analisador léxico
def analisador_lexico_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return analisador_lexico(arquivo)

# Exemplo de uso
nome_arquivo = "texto.cic"  # Substitua pelo nome do seu arquivo
tokens = analisador_lexico_arquivo(nome_arquivo)
for token, lexema in tokens:
    print(f"Token: {token}, Lexema: {lexema}")