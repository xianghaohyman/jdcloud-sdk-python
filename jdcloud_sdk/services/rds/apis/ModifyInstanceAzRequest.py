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


class ModifyInstanceAzRequest(JDCloudRequest):
    """
    修改实例的可用区，例如将实例的可用区从单可用区调整为多可用区
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyInstanceAzRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyInstanceAz', 'POST', header, version)
        self.parameters = parameters


class ModifyInstanceAzParameters(object):

    def __init__(self, regionId, instanceId, newAzId):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param newAzId: 新可用区ID。 如果是单机实例，只需输入一个可用区；如果是主备实例，则必须输入两个可用区ID：第一个为主节点所在可用区，第二个为备节点所在可用区。主备两个可用区可以相同，也可以不同
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.newAzId = newAzId
