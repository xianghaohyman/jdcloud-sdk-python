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


class RRInfo(object):

    def __init__(self, creator=None, viewName=None, id=None, hostRecord=None, hostValue=None, jcloudRes=None, mxPriority=None, port=None, ttl=None, type=None, weight=None, viewValue=None, resolvingStatus=None, updateTime=None):
        """
        :param creator: (Optional) 创建者
        :param viewName: (Optional) 线路名称
        :param id: (Optional) 域名解析的唯一ID
        :param hostRecord: (Optional) 主机记录
        :param hostValue: (Optional) 解析记录的值
        :param jcloudRes: (Optional) 是否是京东云资源
        :param mxPriority: (Optional) 优先级，只存在于MX, SRV解析记录类型
        :param port: (Optional) 端口，只存在于SRV解析记录类型
        :param ttl: (Optional) 解析记录的生存时间，单位：秒
        :param type: (Optional) 解析记录的类型，请参考<a href="https://docs.jdcloud.com/cn/jd-cloud-dns/detailed-interpretation-of-parsed-records">解析记录类型详解</a>
        :param weight: (Optional) 解析记录的权重
        :param viewValue: (Optional) 解析线路的ID
        :param resolvingStatus: (Optional) 解析记录的状态，正常解析:2，暂停解析:4
        :param updateTime: (Optional) 解析记录更新的时间
        """

        self.creator = creator
        self.viewName = viewName
        self.id = id
        self.hostRecord = hostRecord
        self.hostValue = hostValue
        self.jcloudRes = jcloudRes
        self.mxPriority = mxPriority
        self.port = port
        self.ttl = ttl
        self.type = type
        self.weight = weight
        self.viewValue = viewValue
        self.resolvingStatus = resolvingStatus
        self.updateTime = updateTime
