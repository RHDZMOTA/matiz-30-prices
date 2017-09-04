import os
from conf.settings import DataFilesConf


def create_dirs(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)


if __name__ == '__main__':
    create_dirs(DataFilesConf.Paths.data)
    create_dirs(DataFilesConf.Paths.output)

