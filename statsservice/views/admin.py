#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from statsservice.views.common import admin_permission


# import statsservice.lib.processors
# from statsservice.models import Client, Stats


# stats_bp: blueprint for
admin_bp = Blueprint("admin_bp", __name__, url_prefix="/admin")


@admin_bp.route("/client_sharing_activate.json/<client_uuid>", methods=["GET"])
@login_required
@admin_permission.require(http_exception=403)
def client_sharing_activate(client_uuid):
    """Enable the sharing of stats for a client."""
    env = os.environ.copy()
    env["FLASK_APP"] = "runserver.py"
    cmd = [
        sys.exec_prefix + "/bin/flask",
        "client_sharing_activate",
        "--uuid",
        str(client_uuid),
    ]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env)
    # stdout, stderr = process.communicate()
    # print(stdout)

    return jsonify({"result": "OK"})


@admin_bp.route("/client_sharing_deactivate.json/<client_uuid>", methods=["GET"])
def client_sharing_deactivate(client_uuid):
    """Disable the sharing of stats for a client."""
    env = os.environ.copy()
    env["FLASK_APP"] = "runserver.py"
    cmd = [
        sys.exec_prefix + "/bin/flask",
        "client_sharing_deactivate",
        "--uuid",
        str(client_uuid),
    ]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env)
    # stdout, stderr = process.communicate()
    # print(stdout)

    return jsonify({"result": "OK"})


@admin_bp.route("/update.json", methods=["GET"])
def update():
    pass
