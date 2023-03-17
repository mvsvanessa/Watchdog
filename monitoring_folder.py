# https://pythonhosted.org/watchdog/quickstart.html
# https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module
# https://stackoverflow.com/questions/15318208/capture-control-c-in-python
import os
import sys
import time
import logging
from datetime import date

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import platform

folder1 = 'C:/Users/auc2ca/PycharmProjects/monitoring_folders'
folder2 = 'S:/PM/ter/ets/Inter_Setor/COMPARTILHADO'

if __name__ == "__main__":

    logging.basicConfig(filename=str(date.today()) + '.txt',
                        filemode="a",
                        format=f'%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, folder2, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
