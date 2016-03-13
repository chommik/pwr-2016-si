# -*- coding: utf-8 -*-
import logging


def setup_logging():
    log_format = "{asctime} {levelname:8} {threadName:<15} [{module}:{lineno}] {message}"
    logging.basicConfig(format=log_format, style="{", level=logging.DEBUG)


def main():
    setup_logging()
    logging.critical("DUPA")


if __name__ == "__main__":
    main()