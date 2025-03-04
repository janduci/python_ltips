import sys

def validar_argumentos(args):
    if len(args) < 2 or len(args) > 2:
        print("Uso: python script.py NEW")
        sys.exit(1)
    
    primeiro_argumento = args[1]


    if primeiro_argumento != "NEW":
        print("Erro: O segundo argumento deve ser 'NEW'")
        sys.exit(1)

def obter_dados_do_usuario():
    nome_arquivo = input("Digite o nome do arquivo (com extensão .txt): ")
    if not nome_arquivo.endswith('.txt'):
        print("Erro: O arquivo deve ter a extensão .txt")
        sys.exit(1)
    
    tag = input("Digite a tag: ")
    comentario = input("Digite o comentário: ")
    
    return nome_arquivo, tag, comentario

def escrever_no_arquivo(nome_arquivo, tag, comentario):
    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f"{tag}\n")
            arquivo.write(f"{comentario}\n")
        print(f"Tag e comentário foram escritos no arquivo {nome_arquivo}.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validar_argumentos(sys.argv)
    nome_arquivo, tag, comentario = obter_dados_do_usuario()
    escrever_no_arquivo(nome_arquivo, tag, comentario)
