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


# Função para identificar tokens
def identificar_token(lexema):
    if re.match(r'^([A-F0-9]+(\.[A-F0-9]+)?([eE][\+\-]?[0-9]+)?)$', lexema):
        return "TK_NUMERO"
    elif re.match(r'^[A-Z]+\d*(\.\d{2})?$', lexema):
        return "TK_MOEDA"
    elif re.match(r'^[-~+*/&!=<>:|]+$', lexema):
        return "TK_OPERADOR"
    elif re.match(r'^[(,)]+$', lexema):
        return "TK_DELIMITADORES"
    elif re.match(r'^"[a-zA-Z0-9 .]*"$', lexema):
        return "TK_CADEIA"
    else:
        return "TK_DESCONHECIDO"

# Função principal do analisador léxico
def analisador_lexico(codigo_fonte):
    estado_atual = Q0
    lexema = ""
    tokens = []

    for char in codigo_fonte:
        if estado_atual == Q0:
            if char.isalpha() or char.isdigit():
                estado_atual = Q41
                lexema = char  # Começar novo lexema
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
            
                
            elif char.isspace():
                continue
            else:
                # Caractere não reconhecido, trate o erro aqui
                pass

        elif estado_atual == Q1:
            lexema += char
            print('entrou Q1', lexema)
            if char.isalpha() or char.isdigit():
                estado_atual = Q2
        elif estado_atual == Q2:
            lexema += char
            if char == '"':
                estado_atual = Q3
                print('entrou Q2', lexema, estado_atual, char)
        elif estado_atual == Q3:
                print('entrou no estado final', lexema)
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                print(token)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0
                
        
        elif estado_atual == Q41:
            if char.isalpha() or char.isdigit() or char == '.':
                lexema += char
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


        #lexema de ~
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
            if char == '>':
                lexema += char

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
                '''print('entrou', lexema , estado_atual)'''
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
                ''' print('entrou', lexema , estado_atual) '''
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
            if char == '(':
                lexema += char
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0

        elif estado_atual == Q30:
            if char == ')':
                lexema += char
            else:
                # Identifique o token com base no lexema atual e adicione-o à lista de tokens
                token = identificar_token(lexema)
                if token != "TK_DESCONHECIDO":
                    tokens.append((token, lexema))
                # Reinicie o lexema e volte ao estado inicial
                lexema = ""
                estado_atual = Q0


        # COMENTARIO DE LINHA
        

        #LEXEMAS COMENTARIO
        elif estado_atual == Q22:
            if char == "'":
                lexema += char
                estado_atual = Q23
                print('entrou aq')


                

        elif estado_atual == Q23:
            if char == "'":
                lexema += char
                estado_atual = Q24



        elif estado_atual == Q24:
            if char.isdigit() or char.isalpha():
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
                    print(token,lexema)
                    if token != "TK_DESCONHECIDO":
                        tokens.append((token, lexema))
                    # Reinicie o lexema e volte ao estado inicial
                    lexema = ""
                    estado_atual = Q0
                    
        
      




 
        # Implemente outros estados e transições...



    return tokens

# Função para ler o conteúdo do arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

# Exemplo de uso
nome_arquivo = "texto.cic"  # Substitua pelo nome do seu arquivo
codigo_fonte = ler_arquivo(nome_arquivo)
tokens = analisador_lexico(codigo_fonte)
for token, lexema in tokens:
    print(f"Token: {token}, Lexema: {lexema}")