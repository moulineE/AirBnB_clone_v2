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


def do_deploy(archive_path):
    """a function that distributes an archive to my web servers"""
    if not os.path.isfile(archive_path):
        return (False)
    tar_f_name = archive_path.split("/")[-1]
    tar_name_WO_ext = tar_f_name.split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}".
            format(tar_name_WO_ext))
        run("sudo tar xzf /tmp/{} -C /data/web_static/releases/{}".
            format(tar_f_name, tar_name_WO_ext))
        run("sudo rm /tmp/{}".format(tar_f_name))
        run("sudo mv /data/web_static/releases/{}/\
             web_static/* /data/web_static/releases/{}".
            format(tar_name_WO_ext, tar_name_WO_ext))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(tar_name_WO_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".
            format(tar_name_WO_ext))
        return (True)
    except Exception:
        return (False)
