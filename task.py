#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import os
from invoke import task, Collection, Program


def docker_compose(c, cmd, **kwargs):
    """Fun"""
    command = ["docker-compose"]
    for config_file in c.docker_compose_files:
        command.append("-f")
        command.append(config_file)

    command.append(cmd)
    command.insert(0, "export USERID=$UID && export GROUPID=$GID &&")

    return c.run(" ".join(command), **kwargs)

@task
def python(c, cmd, **kwargs):
    """The function is used to start a command inside a container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} fedora python3 /program/{cmd}", pty=True)


@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "build")


MAIN_COLLECTION = Collection()

LOCAL_NS = Collection("local")
LOCAL_NS.configure({
    "docker_compose_files": [
        "./docker-compose.yml"
    ]
})
MAIN_COLLECTION.add_collection(LOCAL_NS)

LOCAL_NS.add_task(rebuild)
LOCAL_NS.add_task(python)

PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
