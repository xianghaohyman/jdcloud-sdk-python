# coding=utf8

# Copyright 2018 JDCLOUD.COM
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
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class StartPipelineRequest(JDCloudRequest):
    """
    根据uuid启动一个流水线任务
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(StartPipelineRequest, self).__init__(
            '/regions/{regionId}/pipeline/{uuid}:start', 'POST', header, version)
        self.parameters = parameters


class StartPipelineParameters(object):

    def __init__(self, regionId, uuid, ):
        """
        :param regionId: Region ID
        :param uuid: 流水线uuid
        """

        self.regionId = regionId
        self.uuid = uuid

