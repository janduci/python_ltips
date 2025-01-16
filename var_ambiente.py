# convenção, documentação, metadatas do Python
__version__ = "0.0.1"
__author__ = "Janduci"
__license__ = "Unlicense"

# modúlo "os" para interagir com Sistema Operacional
# para obter ajuda sobre o módulo, basta entrat no shell linux e digitar python3, importar o modulo os e após isso digitar help(os)
import os 

# os.environ -> um dicionário Python contendo as variavéis e seus valoresq
# os.getenv("LANG") -> função usada para buscar o valor de uma variável especifica.

current_language = os.getenv("LANG", "en_US")[:5]
message = "Hello, World!"

if current_language == "pt_BR":
    message = "Olá, Mundo!"
elif current_language == "it_IT":
    message = "Ciao, Mondo!"
elif current_language == "es_ES":
    message = "Hola, Mundo!"

print(message)  
                                                                                            
# uma forma de forçar uma variável é declará-la na frente do Python. Exemplo: LANG=it_IT python3 var_ambiente.py
