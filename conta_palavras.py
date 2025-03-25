def contar_letras(nome_arquivo):
    try:
        # Abre o arquivo em modo de leitura
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
        
        # Filtra apenas as letras (ignorando espaços, números e caracteres especiais)
        letras = [char for char in conteudo if char.isalpha()]
        
        # Conta as letras
        quantidade_letras = len(letras)
        
        print(f"Quantidade de letras no arquivo '{nome_arquivo}': {quantidade_letras}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Nome do arquivo
arquivo_nome = "alice.txt"  # Substitua pelo nome do seu arquivo
contar_letras(arquivo_nome)
