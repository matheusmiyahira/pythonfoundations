import logging

logging.basicConfig(
    filename='aula10.log',
    level= logging.DEBUG,
    format='%(asctime)s [ %(levelname)s ] %(name)s\n %(funcName)s [%(filename)s, %(lineno)s ] %(message)s',
    # 22:00 [info] python app [app.py, 23] module not found.
    datefmt= '[ %d/%m/%Y %H:%M:%S ]'
)

logging.debug('Mensagem de Debug')
logging.info('Mensagem de info')
logging.warning('Mensagem de Warning')
logging.error('Mensagem de error')
logging.critical('Mensagem de Debug')

#Usando logs

def soma(n1,n2):
    return n1 + n2
try:
    a = soma(3,'n')
    logging.info(f'Soma efetuada com sucesso, resultado {a}')
    print(a)
except TypeError as e:
    logging.error(e)




