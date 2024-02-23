    import pigpio
except ModuleNotFoundError as e:
    from modules.mocks.mock_pigpio import MockPiGPIO
    import pigpio
    from modules.mocks.mock_cv2 import MockCV2

from time import sleep, time
import signal
import schedule
add here later

if Config.get('vision', 'tech') == 'opencv':
    from modules.opencv.vision import Vision
    from modules.opencv.tracking import Tracking
    from modules.opencv.train_model import TrainModel
    from modules.opencv.video_stream import VideoStream
    from modules.opencv.timelapse import Timelapse
elif Config.get('vision', 'tech') == 'coral':
    from modules.coral.vision import Vision
    from modules.coral.tracking import Tracking



def mode():
    if len(sys.argv) > 1 and sys.argv[1] == 'manual':
        return Config.MODE_KEYBOARD
    return Config.MODE_LIVE
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(26, GPIO.FALLING)
