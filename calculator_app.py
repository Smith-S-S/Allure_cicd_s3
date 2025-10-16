import subprocess
import pyautogui
import time

class RealCalculator:
    def __init__(self):
        self.process = None

    def open(self):
        self.process = subprocess.Popen("calc.exe")
        time.sleep(1.5)

    def type_input(self, value):
        pyautogui.write(str(value))
        time.sleep(0.5)

    def close(self):
        if self.process:
            self.process.terminate()
            time.sleep(1)
