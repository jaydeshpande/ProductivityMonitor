import platform
from AppKit import NSWorkspace
from application_base_class import application_properties
import time
import os
from datetime import datetime
import csv

#TODO parent directory is needed when activity tracker starts working over several days
parent_directory = os.getcwd()

class activity_scanner:
    application_names = []
    application_directory = {}
    scanner_start_time = datetime.today()
    storage_folder = str(scanner_start_time.year) + '-' + \
                     str(scanner_start_time.month) + '-' + str(scanner_start_time.day)
    storage_directory = parent_directory + '/' + storage_folder
    if (os.path.isdir(storage_directory)) == True:
        os.chdir(storage_directory)
        if (os.path.isfile('timeHistory.csv')==True):
            os.remove('timeHistory.csv')
    else:
        os.mkdir(storage_directory)
        os.chdir(storage_directory)
    with open('timeHistory.csv', 'a') as csvfile:
        fieldnames = ['timestamp', 'instance' , 'Application', 'timeHistory']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    @staticmethod
    def get_window_title():
        if (platform.system() == 'Darwin'):
            active_app_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
            return active_app_name
        else:
            openwindow = None
            # openwindow = win32gui.GetWindowText (w.GetForegroundWindow())
            # TODO developing this on Mac - to be tested on windows separately
            return openwindow
    def check_if_app_exists(self):
        current_active = self.get_window_title()
        if current_active in activity_scanner.application_names:
            activity_scanner.application_directory[current_active].update_time_objects()
        else:
            activity_scanner.application_names.append(current_active)
            activity_scanner.application_directory[current_active] = application_properties(current_active)

def run():
    today = activity_scanner()
    while(1):
        today.check_if_app_exists()
        time.sleep(2)
        app = today.get_window_title()

if __name__ == "__main__":
    run()