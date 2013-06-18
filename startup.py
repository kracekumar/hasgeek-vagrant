#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import os
import sys
from fabric.api import run, cd, env

GITHUB_URL_PATTERN = "git@github.com:hasgeek/%s.git"
HASGEEK_DEPENDENCIES = ['flask-lastuser', 'coaster', 'baseframe', 'lastuser', 'flask-commentease']
HASGEEK_REPOS = ['hasgeek.tv', 'hacknight', 'hasjob', 'peopleflow', 'contactpoint', 'imgee', 'kharcha']
CLONE_BASE_DIR = os.getenv("HOME") + os.path.sep + 'hasgeek'
INSTALL_BASE_DIR = "/vagrant/hasgeek"


# set env.hosts for local setup
def local():
    env.hosts = ['localhost']


def vagrant():
    env.user = "vagrant"
    env.password = "vagrant"


def clone(repo, base_dir):
    sys.stdout.write("All repos will be cloned to %s\n" % (base_dir))
    if not os.path.isdir(base_dir):
        os.mkdir(base_dir)
    with cd(base_dir):
        if os.path.isdir(repo):
            sys.stdout.write("%s repo exists ...\n" % (repo))
        else:
            run("git clone %s \n" % (GITHUB_URL_PATTERN % repo))


def clone_hasgeek_dependencies(base_dir=CLONE_BASE_DIR):
    for repo in HASGEEK_DEPENDENCIES:
        clone(repo=repo, base_dir=base_dir)


def clone_hasgeek_repos(base_dir=CLONE_BASE_DIR):
    for repo in HASGEEK_REPOS:
        clone(repo=repo, base_dir=base_dir)


def install(base_dir=INSTALL_BASE_DIR):
    all_dirs = os.listdir(base_dir)
    for directory in all_dirs:
        path = base_dir
        if path.endswith(os.path.sep):
            path += directory
        else:
            path += os.path.sep + directory
        with cd(path):
            os.chdir(path)
            if os.path.exists('setup.py'):
                run("sudo python setup.py develop")
                if directory == 'baseframe':
                    run("cd baseframe")
                    run("make")
            elif os.path.exists("requirements.txt"):
                run("sudo pip install -r requirements.txt")
            else:
                sys.stdout.write("couldn't find requirements.txt and setup.py file in %s \n" % (path))
