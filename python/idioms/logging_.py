"""
Logging in python can be finicky

https://stackoverflow.com/questions/43109355/logging-setlevel-is-being-ignored

https://stackoverflow.com/a/66345269/9518712

"""
import logging
import sys

logger = logging.getLogger(__name__)


def configure_logging(verbosity: int = 0) -> None:
    """Configure logging verbosity for the application.
    Whitelist log modules.

    Levels:
       0 (default): WARNING
       1      (-v): INFO
       2     (-vv): DEBUG

    :param verbosity: The logger level to use.
    """
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s.%(funcName)s:%(lineno)d %(message)s"
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    # Silence other loggers
    for log_name, log_obj in logging.Logger.manager.loggerDict.items():
        if log_name != __name__:
            log_obj.disabled = True


# def configure_logging(verbosity: int) -> None:
#     """Configure logging with external libraries.

#     Levels:
#        0 (default): ("cerebro") = INFO,  ("hdal","hubble_direct") = WARNING
#        1      (-v): ("cerebro") = DEBUG, ("hdal","hubble_direct") = WARNING
#        2     (-vv): ("cerebro") = DEBUG, ("hdal","hubble_direct") = INFO
#        3    (-vvv): ("cerebro") = DEBUG, ("hdal","hubble_direct") = DEBUG

#     Note: ("csolace", "h2", "hpack", "ddo_utils.stores") are always WARNING
#     """
#     logging.basicConfig(
#         level=logging.DEBUG if verbosity else logging.INFO,
#         format="%(asctime)s %(levelname)s %(name)s.%(funcName)s:%(lineno)d %(message)s",
#     )

#     for handle in ("hdal", "hubble_direct"):
#         level = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}.get(
#             verbosity, logging.DEBUG
#         )
#         logging.getLogger(handle).setLevel(level)

#     for handle in ("csolace", "h2", "hpack", "ddo_utils.stores"):
#         logging.getLogger(handle).setLevel(logging.WARNING)


# def configure_logging(verbosity: int = 0) -> None:
#     """Configure logging verbosity for the application.

#     Levels:
#        0 (default): WARNING
#        1      (-v): INFO
#        2     (-vv): DEBUG

#     :param verbosity: The logger level to use.
#     """
#     level = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}
#     logging.basicConfig(level=level.get(verbosity, logging.DEBUG))
#     for handle in ("invoke"):
#         logging.getLogger(handle).setLevel(logging.WARNING)

# # remove default handler so we only print to stdout
# logging.getLogger().removeHandler(logging.getLogger().handlers[0])
# stream_handler = logging.StreamHandler(sys.stdout)
# format_str = (
#     "%(asctime)s %(levelname)s %(name)s.%(funcName)s:%(lineno)d %(message)s"
# )
# stream_handler.setFormatter(logging.Formatter(format_str))
# logging.getLogger().addHandler(stream_handler)
