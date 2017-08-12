import platform
from AppKit import NSWorkspace
from application_base_class import application_properties
import time

class activity_scanner:
    application_names = []
    application_directory = {}
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

if __name__ == "__main__":
    today = activity_scanner()
    while(1):
        today.check_if_app_exists()
        time.sleep(2)
        app = today.get_window_title()
        #print (activity_scanner.application_directory[app].timeHistory)