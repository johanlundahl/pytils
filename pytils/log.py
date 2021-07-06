from datetime import datetime
import __main__
import logging
import os


def init(log_name='application'):
    file_name = '{}.log'.format(log_name)
    msg_format = '%(asctime)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=file_name,
                        filemode='w',
                        format=msg_format,
                        datefmt=date_format,
                        level=logging.INFO)


def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        elapsed = datetime.now() - start
        print('{} elapsed in {}'.format(func.__name__, elapsed))
        return res
    return wrapper


def called_at(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print('{} {}{}'.format(start, func.__name__, args))
        return func(*args, **kwargs)
    return wrapper


def auto_name_log():
    main_module = os.path.splitext(os.path.basename(__main__.__file__))[0]
    init(main_module)
