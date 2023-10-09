#!/usr/bin/python3
"""
 a Fabric script (based on the file 2-do_deploy_web_static.py)
 that creates and distributes an archive to your web servers,
 using the function deploy
"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = [
    '100.26.9.80',
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
        run("sudo mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}".
            format(tar_name_WO_ext, tar_name_WO_ext))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(tar_name_WO_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".
            format(tar_name_WO_ext))
        print('New version deployed!')
        return (True)
    except Exception:
        return (False)


def do_pack():
    """fuction that generates the .tgz archive"""
    local("mkdir -p versions")
    tar_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static".format(tar_name))
    if result.failed:
        return None
    else:
        return tar_name


def deploy():
    """a function that call do_pack and do_deploy"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
