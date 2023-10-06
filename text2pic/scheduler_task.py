import datetime
import os


def scheduled_task(folder_path):
    """
    A task that runs in some interval and deletes all the images
    found in the /static folder that are older than some threshold
    :type folder_path: the folder to clean
    :return: nothing
    """
    deleted_files = 0
    threshold_time = datetime.datetime.now() - datetime.timedelta(minutes=5)
    pending = os.listdir(folder_path)
    if not pending:
        print(f'Scheduled task to remove old images: nothing to do')
        return
    for file in pending:
        filename, extension = os.path.splitext(file)
        # file_time = time.mktime(filename)
        file_time = datetime.datetime.strptime(filename, '%Y%m%d_%H%M%S_%f')
        if threshold_time > file_time:
            # print('\tolder than 5 minutes, deleting...')
            os.remove(os.path.join(folder_path, file))
            deleted_files += 1
    print(f'Scheduled task to remove old images: {datetime.datetime.now()}. '
          f'{deleted_files} files deleted out of {len(pending)}')
