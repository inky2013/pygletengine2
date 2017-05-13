import logging

def generate_logger(name: str, log_level: str="INFO") -> logging.Logger:
    logger = logging.getLogger(name)
    log_level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(log_level)
    fmt = '[%(asctime)s] [%(module)s/%(levelname)s]: %(message)s'
    fmt_date = '%H:%M:%S'
    formatter = logging.Formatter(fmt, fmt_date)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger