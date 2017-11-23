import datetime
import os
import time
from app import app


def scheduled_task():
    """
    A task that runs in some interval and deletes all the images
    found in the /static folder that are older than some threshold
    :return:
    """
    # time.mktime(time_str)
    # iterate all image files in the static folder
    folder_path = app.static_folder
    total_files = 0
    deleted_files = 0
    threshold_time = datetime.datetime.now() - datetime.timedelta(minutes=30)
    for file in sorted(os.listdir(folder_path)):
        #print('File: ' + file)
        total_files += 1
        filename, extension = os.path.splitext(file)
        if extension == '.png':
            # file_time = time.mktime(filename)
            file_time = datetime.datetime.fromtimestamp(float(filename))
            if threshold_time > file_time:
                #print('\tolder than 5 minutes, deleting...')
                os.remove(os.path.join(folder_path, file))
                deleted_files += 1
    print('Scheduled task to remove old images: %s' + datetime.now() + '. ' + deleted_files
          + ' files deleted out of ' + total_files)
