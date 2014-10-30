# -*- coding: utf-8 -*-

__author__ = 'Syn'

from Shooter_hash import ShooterHash
from urllib import urlencode
from urllib2 import Request, urlopen
import json


class Shooter(object):
    """
    实现射手网api
    """

    shooter_url = "http://shooter.cn/api/subapi.php"

    filename = ""
    movie_hash = ""

    subs_info = []

    def start(self):
        self.movie_hash = ShooterHash.compute_file_hash(self.filename)
        values = dict(filehash=self.movie_hash, pathinfo=self.filename, format="json", lang="Chn")
        data = urlencode(values).encode('utf-8', 'replace')
        req = Request(self.shooter_url, data)
        rsp = urlopen(req)
        content = rsp.read().decode('utf-8', 'replace')

        json_content = json.loads(content)
        for idx_i, i in enumerate(json_content):
            print(i)

            if i["Delay"] != 0:
                delay_filename = '.'.join((self.filename, "chn%s" % ("" if idx_i == 0 else idx_i), "delay"))
                with open(delay_filename, 'w') as output:
                    output.write(str(i["Delay"]))
            for idx_j, j in enumerate(i["Files"]):
                out_filename_list = [self.filename, "chn%s" % ("" if idx_i == 0 else idx_i), str(j["Ext"])]
                if len(i["Files"]) != 1:
                    out_filename_list.insert(2, str(idx_j))
                out_filename = '.'.join(out_filename_list)
                download_link = j["Link"]
                print(download_link)
                response = urlopen(download_link)
                download_content = response.read()
                with open(out_filename, 'wb') as output:
                    output.write(download_content)

    def __init__(self, params):
        """
        Constructor
        """
        self.filename = params
