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


class ModifyServerGroupRequest(JDCloudRequest):
    """
    修改虚拟服务器组
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyServerGroupRequest, self).__init__(
            '/regions/{regionId}/serverGroups/{serverGroupId}', 'POST', header, version)
        self.parameters = parameters


class ModifyServerGroupParameters(object):

    def __init__(self, regionId, serverGroupId, ):
        """
        :param regionId: 地域ID，可调用接口（queryCPSLBRegions）获取云物理服务器支持的地域
        :param serverGroupId: 服务器组ID
        """

        self.regionId = regionId
        self.serverGroupId = serverGroupId
        self.name = None

    def setName(self, name):
        """
        :param name: (Optional) 名称
        """
        self.name = name
