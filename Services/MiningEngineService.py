import keyboard
import pyautogui
import pydirectinput
import time


from Services.Logger import Logger
from Services.ApplicationConfigReader import ApplicationConfigReader


class MiningEngineService:

    def __init__(self):

        self.config = ApplicationConfigReader("Config/app_config.txt")
        self.logger = Logger(self.config.readFromConfigFile("basic_mining_engine_log_path"))

    def start_mining(self):

        self.logger.log_message("Mining engine started")
        while not keyboard.is_pressed('q'):

            if keyboard.is_pressed('u'):
                self.logger.log_message("Mining started")
                pyautogui.mouseDown()

            if keyboard.is_pressed('i'):
                self.logger.log_message("Mining interrupted", "warning")
                pyautogui.mouseUp()

        self.logger.log_message("Mining engine stopped", "warning")

