__author__ = 'Syn'

import os
import hashlib


class ShooterHash(object):
    """
    shooter的文件hash计算
    https://docs.google.com/document/d/1w5MCBO61rKQ6hI5m9laJLWse__yTYdRugpVyz4RzrmM/preview#
    """
    @staticmethod
    def compute_file_hash(filename):
        try:
            f = open(filename, "rb")
        except IOError:
            print("Cannot read file %s" % filename)

        stat_info = os.stat(filename)
        file_length = stat_info.st_size

        ret = []
        for i in (4096, int(file_length / 3) * 2, int(file_length / 3), file_length - 8192):
            f.seek(i, 0)
            buf = f.read(4096)
            ret.append(hashlib.md5(buf).hexdigest())
        f.close()

        return ';'.join(ret)

    def __init__(self):
        """
        Constructor
        """