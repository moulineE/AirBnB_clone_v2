#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """fuction that generates the .tgz archive"""
    local("mkdir -p versions")
    tar_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static".format(tar_name))
    if result.failed:
        return None
    else:
        return print(tar_name)
