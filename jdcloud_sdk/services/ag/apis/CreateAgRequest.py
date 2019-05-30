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


class CreateAgRequest(JDCloudRequest):
    """
    创建一个高可用组
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateAgRequest, self).__init__(
            '/regions/{regionId}/availabilityGroups', 'POST', header, version)
        self.parameters = parameters


class CreateAgParameters(object):

    def __init__(self, regionId, azs, agName, instanceTemplateId, ):
        """
        :param regionId: 地域
        :param azs: 支持的可用区，最少一个
        :param agName: 高可用组名称，只支持中文、数字、大小写字母、英文下划线 “_” 及中划线 “-”，且不能超过 32 字符
        :param instanceTemplateId: 实例模板的Id
        """

        self.regionId = regionId
        self.azs = azs
        self.agName = agName
        self.agType = None
        self.instanceTemplateId = instanceTemplateId
        self.description = None

    def setAgType(self, agType):
        """
        :param agType: (Optional) 高可用组类型，支持vm
        """
        self.agType = agType

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，长度不超过 256 字符
        """
        self.description = description
