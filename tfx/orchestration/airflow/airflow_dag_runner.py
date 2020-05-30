# Lint as: python2, python3
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Definition of Airflow TFX runner."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os  # pylint: disable=unused-import
from typing import Any, Dict, Optional, Text, Union

import absl
from airflow import models  # pylint: disable=unused-import

from tfx.orchestration import pipeline
from tfx.orchestration import tfx_runner
from tfx.orchestration.airflow import airflow_component  # pylint: disable=unused-import
from tfx.orchestration.config import config_utils  # pylint: disable=unused-import
from tfx.orchestration.config import pipeline_config


class AirflowPipelineConfig(pipeline_config.PipelineConfig):
  """Pipeline config for AirflowDagRunner."""

  def __init__(self, airflow_dag_config: Dict[Text, Any] = None, **kwargs):
    """Creates an instance of AirflowPipelineConfig.

    Args:
      airflow_dag_config: Configs of Airflow DAG model. See
        https://airflow.apache.org/_api/airflow/models/dag/index.html#airflow.models.dag.DAG
          for the full spec.
      **kwargs: keyword args for PipelineConfig.
    """

    super(AirflowPipelineConfig, self).__init__(**kwargs)
    self.airflow_dag_config = airflow_dag_config or {}


class AirflowDagRunner(tfx_runner.TfxRunner):
  """Tfx runner on Airflow."""

  def __init__(self,
               config: Optional[Union[Dict[Text, Any],
                                      AirflowPipelineConfig]] = None):
    """Creates an instance of AirflowDagRunner.

    Args:
      config: Optional Airflow pipeline config for customizing the launching of
        each component.
    """
    if config and not isinstance(config, AirflowPipelineConfig):
      absl.logging.warning(
          'Pass config as a dict type is going to deprecated in 0.1.16. Use AirflowPipelineConfig type instead.',
          PendingDeprecationWarning)
      config = AirflowPipelineConfig(airflow_dag_config=config)
    super(AirflowDagRunner, self).__init__(config)

  def run(self, tfx_pipeline: pipeline.Pipeline):
    """Deploys given logical pipeline on Airflow.

    Args:
      tfx_pipeline: Logical pipeline containing pipeline args and components.

    Returns:
      An Airflow DAG.
    """

    return None
