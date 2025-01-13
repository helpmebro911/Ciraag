from time import time

class Ciraag_Uptime:
    def uptime(self):
        try:
            with open("uptime.txt", "r") as f:
                self.start_time = float(f.read())
        except FileNotFoundError:
            with open("uptime.txt", "w") as f:
                self.start_time = time()
                f.write(str(self.start_time))
        self.current_time = time()
        self.uptime = int(self.current_time - self.start_time)
        return self.uptime

def get_uptime():
  ciraag_sys = Ciraag_Uptime()
  uptime = ciraag_sys.uptime()
  hours, remainder = divmod(uptime, 3600)
  minutes, seconds = divmod(remainder, 60)
  ciraag_uptime = f"{hours}h, {minutes}m, {seconds}s"
  return ciraag_uptime