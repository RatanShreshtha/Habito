import logging
import sys

from rich.logging import RichHandler

from src.core.config import settings


def setup_rich_logger():
    """Cycles through uvicorn root loggers to
    remove handler, then runs `get_logger_config()`
    to populate the `LoggerConfig` class with Rich
    logger parameters.
    """

    handler_format = logging.Formatter(settings.log_format, datefmt=settings.log_date_format)

    output_file_handler = logging.FileHandler(settings.log_file)
    output_file_handler.setFormatter(handler_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(handler_format)

    rich_handler = RichHandler(rich_tracebacks=True, tracebacks_show_locals=True, show_time=False)

    handlers = [output_file_handler]

    if settings.debug:
        handlers.append(rich_handler)
    else:
        handlers.append(stdout_handler)

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logging.basicConfig(
        level=settings.log_level,
        format=settings.log_format,
        datefmt=settings.log_date_format,
        handlers=handlers,
    )
