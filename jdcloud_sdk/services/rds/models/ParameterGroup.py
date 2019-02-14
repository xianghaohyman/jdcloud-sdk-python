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


class ParameterGroup(object):

    def __init__(self, parameterGroupId=None, parameterGroupName=None, parameterGroupStatus=None, description=None, engine=None, engineVersion=None, regionId=None, createTime=None):
        """
        :param parameterGroupId: (Optional) 参数组ID
        :param parameterGroupName: (Optional) 参数组名称
        :param parameterGroupStatus: (Optional) 参数组状态
        :param description: (Optional) 参数组描述
        :param engine: (Optional) 实例引擎类型
        :param engineVersion: (Optional) 数据库版本
        :param regionId: (Optional) 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param createTime: (Optional) 参数组创建时间
        """

        self.parameterGroupId = parameterGroupId
        self.parameterGroupName = parameterGroupName
        self.parameterGroupStatus = parameterGroupStatus
        self.description = description
        self.engine = engine
        self.engineVersion = engineVersion
        self.regionId = regionId
        self.createTime = createTime
