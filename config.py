class Config:
    """Configuración global de la aplicación usando el patrón Singleton."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
            cls._instance.data_file = "tasks.json"
        return cls._instance

    def set_debug(self, enabled: bool) -> None:
        self.debug = enabled
