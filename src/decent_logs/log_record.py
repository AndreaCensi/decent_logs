from zuper_commons.logs import ZLoggerInterface

__all__ = [
    "LogRecord",
]


class LogRecord:
    name: str
    timestamp: float
    string: str
    level: str

    def __init__(self, name: str, timestamp: float, string: str, level: str):
        self.name = name
        self.timestamp = timestamp
        self.string = string
        self.level = level

        levels = ["info", "error", "debug", "warn"]
        if not level in levels:
            msg = "Got %r, expected %r." % (level, levels)
            raise ValueError(msg)

    def __str__(self) -> str:
        return "%s: %s" % (self.name, self.string)

    def write_to_logger(self, logger: ZLoggerInterface) -> None:
        s = self.__str__()
        level = self.level
        if level == "info":
            logger.info(s)
        elif level == "error":
            logger.error(s)
        elif level == "debug":
            logger.debug(s)
        elif level == "warn":
            logger.warn(s)
        else:
            assert False
