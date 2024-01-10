#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
        logic function
    """
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    tm = datetime.utcnow()
    arc_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                                                            tm.year,
                                                            tm.month,
                                                            tm.day,
                                                            tm.hour,
                                                            tm.minute,
                                                            tm.second
                                                            )
    res = local("tar -cvzf {} web_static".format(arc_file))
    if res.succeeded:
        return arc_file
    return None
