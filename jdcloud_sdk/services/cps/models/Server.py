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


class Server(object):

    def __init__(self, serverId=None, instanceType=None, instanceName=None, instanceId=None, az=None, privateIp=None, port=None, weight=None, status=None, healthyStatus=None):
        """
        :param serverId: (Optional) 服务器ID
        :param instanceType: (Optional) 资源类型
        :param instanceName: (Optional) 实例名称
        :param instanceId: (Optional) 后端云物理服务器ID
        :param az: (Optional) 可用区
        :param privateIp: (Optional) 内网Ip
        :param port: (Optional) 端口
        :param weight: (Optional) 后端云物理服务器权重
        :param status: (Optional) 状态
        :param healthyStatus: (Optional) 健康状态
        """

        self.serverId = serverId
        self.instanceType = instanceType
        self.instanceName = instanceName
        self.instanceId = instanceId
        self.az = az
        self.privateIp = privateIp
        self.port = port
        self.weight = weight
        self.status = status
        self.healthyStatus = healthyStatus
