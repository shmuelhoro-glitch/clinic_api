import logging


logger = logging.getLogger('clinic_logs')
logger.setLevel(level=logging.INFO)
Formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(message)s",datefmt="%y-%m-%d %H:%M:%S")

if not logger.handlers:
    file_handler = logging.FileHandler("logs/app.log","a",encoding="utf-8")
    file_handler.setFormatter(Formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(Formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    

