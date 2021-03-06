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


class NetworkSecurityGroup(object):

    def __init__(self, networkSecurityGroupId=None, networkSecurityGroupName=None, description=None, vpcId=None, securityGroupRules=None, createdTime=None, networkSecurityGroupType=None, networkInterfaceIds=None):
        """
        :param networkSecurityGroupId: (Optional) 安全组ID
        :param networkSecurityGroupName: (Optional) 安全组名称
        :param description: (Optional) 安全组描述信息
        :param vpcId: (Optional) 安全组所在vpc的Id
        :param securityGroupRules: (Optional) 安全组规则信息
        :param createdTime: (Optional) 安全组创建时间
        :param networkSecurityGroupType: (Optional) 安全组类型, default：默认安全组，custom：自定义安全组
        :param networkInterfaceIds: (Optional) 安全组绑定的弹性网卡列表
        """

        self.networkSecurityGroupId = networkSecurityGroupId
        self.networkSecurityGroupName = networkSecurityGroupName
        self.description = description
        self.vpcId = vpcId
        self.securityGroupRules = securityGroupRules
        self.createdTime = createdTime
        self.networkSecurityGroupType = networkSecurityGroupType
        self.networkInterfaceIds = networkInterfaceIds
