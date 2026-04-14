import threading
import time
import os

from Logger import Logger
from HttpServer import Server_runner
from Prompt import Prompt

# Http server
http_server = Server_runner()

# Prompt
prompt = Prompt()

PORT = 8080

# Threads
threads = []

# Spawn http thread
def spawn_http_server():
    t = threading.Thread(target=http_server.run, args=(PORT,))
    t.start()
    threads.append(t)


# Checksum
start_http_server = True
def checksum():
    Logger.info("Starting checksum...")

    if os.path.isdir("templates"):
        Logger.info('"Templates" directory found')
    else:
        Logger.warn('"Templates" not found, HTTP server wont start')
        global start_http_server
        start_http_server = False

    Logger.info("Checksum finished")

# Main
def main():
    checksum()
    if start_http_server:
        spawn_http_server()

    prompt.run()
    http_server.stop()

    for thread in threads:
        thread.join()

    Logger.info("Exiting main thread...")
    

if __name__ == "__main__":
    main()