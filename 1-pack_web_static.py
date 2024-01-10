#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive from the
    contents of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ A script that generates archive the contents of web_static folder"""
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(time))

        return "versions/web_static_{}.tgz".format(time)
    except Exception as e:
        return None
