from contextlib import contextmanager
from typing import ContextManager, Tuple


class Supressor:
    """Class of a context manager that supressess passed exception.
    :param err: an error which occurs inside the body of the context manager
    :type err: Exception
    """

    def __init__(self, err: Exception):
        self.err = err

    def __enter__(self) -> "Supressor":
        """Enter the runtime context and return this object.
        :return: object of the instance of the class Supressor
        :rtype: Supressor
        """
        return self

    def __exit__(self, exctype: type, *args: Tuple) -> bool:
        """Exit the runtime context and return a Boolean flag
        indicating if any exception that occurred should be suppressed.
        At this context manager such exception will be supressed
        if it was passed to the constructor of the class.

        :param exctype: type of exception that occured inside the body
        of the context manager
        :type exctype: type
        :param args: value and traceback of the occured exception
        :type args: Exception, traceback
        :return: boolean if exception should be supressed
        :rtype: bool
        """
        if issubclass(exctype, self.err):
            return True
        return False


@contextmanager
def supressor(err: Exception) -> ContextManager:
    """Generator which supresses passed exception.
    :param err: Error that should be supressed
    :type err: Exception
    :return: Generator object which supresses passed exception
    as a context manager
    :rtype: Generator
    """
    try:
        yield
    except err:
        pass
