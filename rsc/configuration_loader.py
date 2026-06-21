from typing import Any, Dict
import os
import yaml
from pathlib import Path


class ConfigurationLoader:
    _instances:Dict[str, 'ConfigurationLoader'] = dict()
    _config:Dict[str, Any] = dict()

    def __new__(cls, file_config:str):
        """una instancia por archivo"""
        if file_config not in cls._instances:
            instance = super(ConfigurationLoader, cls).__new__(cls)
            instance._config = dict()
            instance._config_path = Path(file_config)
            instance._load_config()
            cls._instances[file_config] = instance
        return cls._instances[file_config]
    
    def _load_config(self):
        if not self._config_path.exists():
            print(f'no se encontro: {self._config_path}')
            return
        try:
            with open(self._config_path, 'r') as file:
                self._config = yaml.safe_load(file) or {}
        except Exception as err:
            print(f'Error al cargar el archivo de configuracion: {err}')

    def get(self, key_path:str, default:Any=None) -> Any:
        keys = key_path.split('.')
        value = self._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value


base_path = Path(__file__).parent
config_path = f'{base_path}{os.sep}config_sinergia.yml'
settings = ConfigurationLoader(config_path)