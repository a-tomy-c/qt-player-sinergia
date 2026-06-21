from pathlib import Path
import sys
import logging
from datetime import datetime


PROJECT_ROOT = Path(__file__).parent.parent
LOG_DIR = PROJECT_ROOT.joinpath('logs')
LOG_DIR.mkdir(exist_ok=True)


class SinergiaLogger:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        log_file = LOG_DIR.joinpath(f'app_{datetime.now().strftime('%Y%m%d')}.log')
        file_handler =logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        error_file = LOG_DIR.joinpath('errors.log')
        error_handler = logging.FileHandler(error_file, encoding='utf-8')
        error_handler.setLevel(logging.ERROR)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

        root_logger = logging.getLogger()
        root_logger.addHandler(file_handler)
        root_logger.addHandler(error_handler)

        self.logger = logging.getLogger('Sinergia')
        self.logger.info("="*60)
        self.logger.info("Sistema de Logging inicializado.")
        self.logger.info(f"Logs en: {LOG_DIR}")

    def get_logger(self, name:str=None):
        if name:
            return logging.getLogger(f'Sinergia.{name}')
        return self.logger
    
    def debug(self, msg:str):
        self.logger.debug(msg)

    def info(self, msg:str):
        self.logger.info(msg)

    def warning(self, msg:str):
        self.logger.warning(msg)

    def error(self, msg:str):
        self.logger.error(msg)

    def critical(self, msg:str):
        self.logger.critical(msg)
    
    def exception(self, msg:str):
        self.logger.exception(msg)


logger = SinergiaLogger()
