#! /usr/bin/env python
# Stats service API for MONARC
# Copyright (C) 2020-2022 Cédric Bonhomme - https://www.cedricbonhomme.org
# Copyright (C) 2020-2022 SMILE gie securitymadein.lu
#
# For more information: https://github.com/monarc-project/stats-api/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import url_for

from statsservice import __version__
from statsservice.bootstrap import application
from statsservice.models import Client
from statsservice.models import Stats


# root_bp: blueprint of higher level routes
root_bp = Blueprint("root_bp", __name__, url_prefix="")


@root_bp.route("/", methods=["GET"])
def home():
    """For the moment simply redirects to the documentation of the API."""
    return render_template("index.html")


@root_bp.route("evolution", methods=["GET"])
def evolution():
    """The only view of this blueprint which is supposed to return a HTML file.
    Routes defined in the following can be used in this HTML file.
    """
    return render_template("evolution.html")


@root_bp.route("help", methods=["GET"])
def help():
    """About page."""
    return render_template("help.html")


@root_bp.route("about", methods=["GET"])
def about():
    """About page."""
    return render_template("about.html")


@root_bp.route("/about/more", methods=["GET"])
def about_more():
    """Returns some details about the current Stats Service instance."""
    version = __version__.split("-")
    if len(version) == 1:
        stats_service_version = version[0]
        version_url = (
            "https://github.com/monarc-project/stats-service/releases/tag/{}".format(
                version[0]
            )
        )
    else:
        stats_service_version = f"{version[0]} - {version[2][1:]}"
        version_url = (
            "https://github.com/monarc-project/stats-service/commits/{}".format(
                version[2][1:]
            )
        )
    return render_template(
        "about_more.html",
        stats_service_version=stats_service_version,
        version_url=version_url,
        python_version="{}.{}.{}".format(*sys.version_info[:3]),
        nb_contributors=Client.query.count(),
        nb_stats=Stats.query.count(),
    )


@root_bp.route("about.json", methods=["GET"])
def about_json():
    """Provide information about the instance."""
    version = __version__.split("-")
    if len(version) == 1:
        stats_version = version[0]
        version_url = (
            "https://github.com/monarc-project/stats-service/releases/tag/{}".format(
                version[0]
            )
        )
    else:
        stats_version = f"{version[0]} - {version[2][1:]}"
        version_url = (
            "https://github.com/monarc-project/stats-service/commits/{}".format(
                version[2][1:]
            )
        )

    return jsonify(
        version=stats_version,
        version_url=version_url,
        api_v1_root=url_for("api.doc"),
        contact=application.config["ADMIN_EMAIL"],
    )


@root_bp.route("human.txt", methods=["GET"])
def human():
    """Human dot txt page."""
    return render_template("human.txt"), 200, {"Content-Type": "text/plain"}
