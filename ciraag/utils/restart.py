from subprocess import Popen

class Restart_Ciraag:
    def __init__(self):
        self.restart_ciraag = ["python3", "-m", "ciraag"]
        Popen(self.restart_ciraag)