import subprocess
import pyautogui
import time
import cv2
import numpy as np
import pyautogui

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

def record_screen(filename="screen_recording.mp4", duration=5):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, fourcc, 8.0, screen_size)

    start_time = time.time()
    while time.time() - start_time < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    out.release()

