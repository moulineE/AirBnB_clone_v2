#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""
from fabric.api import *
import os

env.hosts = [
    '54.236.44.154',
    '54.237.5.182',
]
if not os.path.isfile(archive_path):
    return False

tar_f_name = archive_path.split("/")[-1]
tar_name-WO_ext = tar_f_name.splt(".")[0]


def do_deploy(archive_path):
    """a function that distributes an archive to my web servers"""
    try:
        put(archive_path, "/tmp/")
        run("tar xzf /tmp/{} /data/web_static/releases/{}".
            format(tar_f_name, tar_name-WO_ext))
        run("rm -f /tmp/{}".format(tar_f_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(tar_name-WO_ext))
        return (True)
    except Exception:
        return (False)
