# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
Task manager api.

This module provides the interfaces to task manage functions.
"""

import os

from flask import Blueprint
from flask import request
from flask import jsonify

from mindinsight.conf import settings
from mindinsight.datavisual.utils.tools import str_to_bool
from mindinsight.datavisual.utils.tools import get_train_id
from mindinsight.datavisual.processors.train_task_manager import TrainTaskManager
from mindinsight.datavisual.data_transform.summary_watcher import SummaryWatcher
from mindinsight.datavisual.data_transform.data_manager import DATA_MANAGER


BLUEPRINT = Blueprint("task_manager", __name__, url_prefix=settings.URL_PREFIX)


@BLUEPRINT.route("/datavisual/single-job", methods=["GET"])
def query_single_train_task():
    """Query single train task"""
    plugin_name = request.args.get('plugin_name')
    train_id = get_train_id(request)

    processor = TrainTaskManager(DATA_MANAGER)
    tasks = processor.get_single_train_task(train_id=train_id, plugin_name=plugin_name)
    return jsonify(tasks)


@BLUEPRINT.route("/datavisual/plugins", methods=["GET"])
def query_plugins():
    """Query plugins."""
    train_id = get_train_id(request)

    manual_update = request.args.get('manual_update', default='false')
    manual_update = str_to_bool(manual_update, "manual_update")

    processor = TrainTaskManager(DATA_MANAGER)
    plugins = processor.get_plugins(train_id, manual_update)
    return jsonify(plugins)


@BLUEPRINT.route("/datavisual/train-jobs", methods=["GET"])
def query_train_jobs():
    """Query train jobs."""
    offset = request.args.get("offset", default=0)
    limit = request.args.get("limit", default=10)

    summary_watcher = SummaryWatcher()
    total, directories = summary_watcher.list_summary_directories_by_pagination(
        settings.SUMMARY_BASE_DIR, offset, limit)

    train_jobs = [{
        'train_id': directory['relative_path'],
        'relative_path': directory['relative_path'],
        'create_time': directory['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
        'update_time': directory['update_time'].strftime('%Y-%m-%d %H:%M:%S'),
    } for directory in directories]

    return jsonify({
        'name': os.path.basename(os.path.realpath(settings.SUMMARY_BASE_DIR)),
        'total': total,
        'train_jobs': train_jobs,
    })


def init_module(app):
    """
    Init module entry.

    Args:
        app: the application obj.

    """
    app.register_blueprint(BLUEPRINT)
