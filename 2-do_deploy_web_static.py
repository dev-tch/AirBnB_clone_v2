#!/usr/bin/python3
"""
 distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
from os.path import exists


env.hosts = ['34.201.164.31', '54.197.101.238']  # <IP web-01>, <IP web-02>


def do_deploy(archive_path):
    """
        logic function
    """
    if not exists(archive_path):
        return False
    try:
        # upload achive to my remote server
        put(archive_path, "/tmp/")
        # get  the name of archive
        file_with_ext = archive_path.split("/")[-1]
        file_no_ext = file_with_ext.split(".")[0]
        # uncompress the archive
        src_path = "/tmp/{}".format(file_with_ext)
        dest_path = "/data/web_static/releases/{}".format(file_no_ext)
        run("tar -xzf {}  -C {}".format(src_path, dest_path))
        # delete achive
        run("rm {}".format(src_path))
        # delete symbolic link
        link = "/data/web_static/current"
        run("rm -rf {}".format(link))
        # recreate new symbolic link
        run("ln -s {} {}".format(dest_path, link))
        return True
    except Exception as e:
        return False
