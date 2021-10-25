import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time


def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):
    for i in range(730, 810):
        for j in range(202, 230):
            if data[i, j] > 100 and data[i, j] < 195:
                hit('up')
                return
    return


if __name__ == '__main__':
    print("Dino game is about to start in 3 seconds")
    time.sleep(4)
    hit('up')
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isCollide(data)
        # print(asarray(image))
    #         for i in range(760, 830):
    #             for j in range(205,250):
    #                 data[i, j] = 0
    # image.show()
