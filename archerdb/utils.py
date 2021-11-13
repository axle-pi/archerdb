"""Define utility methods shared by different files."""
import json

from .constants import get_log_file_path, get_db_dir
from functools import wraps


def log_transaction(func):
    """
    Log a function call and parameters.

    :param func: function called
    :return: function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = list(args)

        log_item = {'class_name': args[0].__class__.__name__,
                    'object_name': args[0].name,
                    'method': func.__name__,
                    'params': args[1:]}
        with open('{}/{}'.format(get_db_dir(),
                                 get_log_file_path()), 'a') as f:
            json.dump(log_item, f)
            f.write('\n')
        return func(*args, **kwargs)
    return wrapper
