import threading

class Logger:
    @staticmethod
    def info(message: str):
        t = threading.current_thread()
        print(f"\033[37m[INFO]{t.name}:{message}\033[0m")
    @staticmethod
    def warn(message: str):
        t = threading.current_thread()
        print(f"\033[33m[WARN]{t.name}:{message}\033[0m")
    @staticmethod
    def error(message: str):
        t = threading.current_thread()
        print(f"\033[31m[ERROR]{t.name}:{message}\033[0m")
    