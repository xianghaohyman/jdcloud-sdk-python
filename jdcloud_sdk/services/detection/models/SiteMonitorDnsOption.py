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


class SiteMonitorDnsOption(object):

    def __init__(self, checkType=None, expectAlias=None, expectIP=None, server=None, timeout=None):
        """
        :param checkType: (Optional) DNS查询类型，可选值：A、MX、NS、CNAME、TXT、ANY，不填默认为A
        :param expectAlias: (Optional) 期望解析别名，多个之间用逗号,分割
        :param expectIP: (Optional) 期望解析ip，多个之间用逗号,分割
        :param server: (Optional) DNS服务器
        :param timeout: (Optional) 
        """

        self.checkType = checkType
        self.expectAlias = expectAlias
        self.expectIP = expectIP
        self.server = server
        self.timeout = timeout
