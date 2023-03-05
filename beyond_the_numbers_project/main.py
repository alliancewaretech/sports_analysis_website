import os
import sys
from load import test
import constants
from data_access_layer import postgres_data_read
class SportsAnalysis():
    def __init__(self) -> None:
        pass

    def start(self):
        try:
            print("Started")

        except:
            print("Exception raised")

        finally:
            print("Final executed")


if __name__=="__main__":
    sports_driver=SportsAnalysis()
    sports_driver.start()
