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
        # get  the name of archive
        file_with_ext = archive_path.split("/")[-1]
        file_no_ext = file_with_ext.split(".")[0]
        # get src and path
        serv_file = "/tmp/{}".format(file_with_ext)
        dir_unzip = "/data/web_static/releases/{}/".format(file_no_ext)
        # upload achive to my remote server
        put(archive_path, "/tmp/")
        # create new directory
        run("mkdir -p {}".format(dir_unzip))
        # uncompress the archive
        run("tar -xzf {}  -C {}".format(serv_file, dir_unzip))
        # move uncompressed files to dir_unzip
        run("mv {}/web_static/* {}/".format(dir_unzip, dir_unzip))
        # remove folder web_static in dir_unzip
        run("rm -rf {}/web_static".format(dir_unzip))
        # delete symbolic link
        link = "/data/web_static/current"
        run("rm -rf {}".format(link))
        # recreate new symbolic link
        run("ln -s {}/ {}".format(dir_unzip, link))
        return True
    except Exception as e:
        return False
