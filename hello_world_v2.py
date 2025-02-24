import os

current_language = os.getenv("LANG", "en_US")[:5]
# a funcao getenv aceita dois argumentos, o primeiro é a variável de ambiente que queremos acessar e o segundo é um valor padrão que será retornado caso a variável de ambiente não exista.
# [:5] é uma operacao de fatiamento é para pegar apenas os 5 primeiros caracteres da variável de ambiente LANG, que é o código do idioma que o usuário está utilizando.

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "es_ES": "¡Hola, Mundo!",
    "fr_FR": "Bonjour, le Monde!",
    "de_DE": "Hallo, Welt!"
}

print(msg[current_language]) 
