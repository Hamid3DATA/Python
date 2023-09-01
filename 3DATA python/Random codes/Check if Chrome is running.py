import psutil


def if_process_is_running_by_exe_name(exe_name='chrome.exe'):
    for proc in psutil.process_iter(['pid', 'name']):
        # This will check if there exists any process running with executable name
        if proc.info['name'] == exe_name:
            return True
    return False


if if_process_is_running_by_exe_name():
    print("It is indeed running!")
else:
    print("It is not currently running!")
