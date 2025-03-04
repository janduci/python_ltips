import logging

# Abaixo estão os níveis de log do Python
# DEBUG numeric value 10
# INFO numeric value 20
# WARNING numeric value 30
# ERROR numeric value 40
# CRITICAL numeric value 50
# NOTSET numereric value 0 # Não é um nível de log, é um valor para desabilitar o log

logging.critical("Erro critico") # Chamando o método critical
# logging.error("Um erro ocorreu") # Chamando o método error
# logging.warning("Aviso de erro") # Chamando o método warning
# logging.info("Informação de erro") # Chamando o método info
# logging.debug("Debug de erro") # Chamando o método debug

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Erro: %s", (e)) # Utilizando %s porque f-string não é compativel com logging
          