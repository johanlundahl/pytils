import logging

def init(log_name = 'application'):
	file_name = '{}.log'.format(log_name)
	msg_format = '%(asctime)s - %(levelname)s - %(message)s'
	date_format = '%Y-%m-%d %H:%M:%S'

	logging.basicConfig(filename=file_name, filemode='w', format=msg_format, datefmt=date_format, level=logging.INFO)

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def error(msg):
    logging.error(msg)

def exception(msg):
	logging.exception(msg)