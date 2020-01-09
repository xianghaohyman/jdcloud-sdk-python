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


class InternalInstance(object):

    def __init__(self, pin=None, region=None, instanceId=None, instanceName=None, instanceType=None, instanceStatus=None, instanceVersion=None, createdTime=None, vpcId=None, subnetId=None, connectionDomain=None, connectionPort=None, auth=None, frontAppIp=None, ips=None, hostIps=None):
        """
        :param pin: (Optional) pin
        :param region: (Optional) region
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称
        :param instanceType: (Optional) 实例类型：master-slave表示主从版，cluster表示集群版
        :param instanceStatus: (Optional) 实例状态：creating表示创建中，running表示运行中，error表示错误，changing表示变更规格中，deleting表示删除中，configuring表示修改参数中，restoring表示备份恢复中
        :param instanceVersion: (Optional) 实例版本：包括2.8、4.0
        :param createdTime: (Optional) 创建时间（ISO 8601标准的UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ）
        :param vpcId: (Optional) 所属VPC的ID
        :param subnetId: (Optional) 所属子网的ID
        :param connectionDomain: (Optional) 访问域名
        :param connectionPort: (Optional) 访问端口
        :param auth: (Optional) 连接redis实例时，是否需要密码认证，false表示无密码
        :param frontAppIp: (Optional) 前端app ip
        :param ips: (Optional) 实例内部节点ip列表
        :param hostIps: (Optional) 实例内部节点所在宿主机ip列表
        """

        self.pin = pin
        self.region = region
        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.instanceStatus = instanceStatus
        self.instanceVersion = instanceVersion
        self.createdTime = createdTime
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.connectionDomain = connectionDomain
        self.connectionPort = connectionPort
        self.auth = auth
        self.frontAppIp = frontAppIp
        self.ips = ips
        self.hostIps = hostIps