import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import platform


folder1 = 'C:/Users/auc2ca/PycharmProjects/monitoring_folders'
folder2 = 'S:/PM/ter/ets/Inter_Setor/COMPARTILHADO'


if __name__ == "__main__":



    logging.basicConfig(level=logging.INFO,
                        format=f'%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

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