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


class InstanceClass(object):

    def __init__(self, instanceClass=None, instanceType=None, cpu=None, memoryMB=None, diskGB=None, maxConnection=None, bandwidthMbps=None):
        """
        :param instanceClass: (Optional) 规格代码：redis 2.8与redis 4.0的规格码不同，具体参考 https://docs.jdcloud.com/cn/jcs-for-redis/specifications
        :param instanceType: (Optional) 规格类型：master-slave表示主从版，cluster表示集群版
        :param cpu: (Optional) cpu核数
        :param memoryMB: (Optional) 内存总容量（MB）
        :param diskGB: (Optional) 磁盘总容量（GB）
        :param maxConnection: (Optional) 最大连接数
        :param bandwidthMbps: (Optional) 内网带宽（MBps）
        """

        self.instanceClass = instanceClass
        self.instanceType = instanceType
        self.cpu = cpu
        self.memoryMB = memoryMB
        self.diskGB = diskGB
        self.maxConnection = maxConnection
        self.bandwidthMbps = bandwidthMbps
