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


main_module = os.path.splitext(os.path.basename(__main__.__file__))[0]
init(main_module)
