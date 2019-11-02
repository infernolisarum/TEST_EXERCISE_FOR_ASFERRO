import logging


class LoggingMix():

    def __getattr__(self, name):
        if name in ['critical', 'error', 'warning', 'info', 'debug']:
            if not hasattr(self.__class__, '_LoggingMix__logger'):
                self.__class__.__logger = logging.getLogger(self.__class__.__module__)
                self.__class__.__logger.setLevel(logging.INFO)
                handler = logging.FileHandler("gmail_tests.log")
                formatter = logging.Formatter("%(levelname)s %(asctime)s %(funcName)s %(lineno)d %(message)s")
                handler.setFormatter(formatter)
                self.__class__.__logger.addHandler(handler)
            return getattr(self.__class__.__logger, name)
        return super(LoggingMix, self).__getattr__(name)
