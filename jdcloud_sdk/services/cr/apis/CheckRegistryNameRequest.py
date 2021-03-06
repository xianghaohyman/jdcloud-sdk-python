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


class CheckRegistryNameRequest(JDCloudRequest):
    """
    查询指定注册表名称是否已经存在以及是否符合命名规范。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CheckRegistryNameRequest, self).__init__(
            '/regions/{regionId}/registries:checkRegistryName', 'POST', header, version)
        self.parameters = parameters


class CheckRegistryNameParameters(object):

    def __init__(self, regionId, registryName):
        """
        :param regionId: Region ID
        :param registryName: 待验证的注册表名。
        """

        self.regionId = regionId
        self.registryName = registryName

