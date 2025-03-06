import logging

# Abaixo estão os níveis de log do Python
# DEBUG numeric value 10
# INFO numeric value 20
# WARNING numeric value 30
# ERROR numeric value 40
# CRITICAL numeric value 50
# NOTSET numereric value 0 # Não é um nível de log, é um valor para desabilitar o log

# logging.critical("Erro critico") # Chamando o método critical
# logging.error("Um erro ocorreu") # Chamando o método error
# logging.warning("Aviso de erro") # Chamando o método warning
# logging.info("Informação de erro") # Chamando o método info
# logging.debug("Debug de erro") # Chamando o método debug

log = logging.Logger("logs", logging.DEBUG) # Criando uma instância de Logger

ch = logging.StreamHandler() # Criando uma instância de StreamHandler
ch.setLevel(logging.DEBUG) # Definindo o nível de log para StreamHandler

fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") # Criando uma instância de Formatter

ch.setFormatter(fmt) # Adicionando o Formatter ao StreamHandler
log.addHandler(ch) # Adicionando o StreamHandler ao Logger

"""    
Logger (log): O principal objeto de logging que gera mensagens de log.
Handler (ch): Um componente que define onde as mensagens de log serão enviadas (neste caso, 
para o console).
Formatter (fmt): Um componente que define o formato das mensagens de log.
Associações: O formatter fmt é associado ao handler ch (ch.setFormatter(fmt)), e o handler 
ch é associado ao logger log (log.addHandler(ch)).
"""  

""" 
log.critical("Erro critico") 
log.error("Um erro ocorreu") 
log.warning("Aviso de erro") 
log.info("Informação de erro")
log.debug("Debug de erro")
"""  

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Erro: %s", (e)) # Utilizando %s porque f-string não é compativel com logging
          