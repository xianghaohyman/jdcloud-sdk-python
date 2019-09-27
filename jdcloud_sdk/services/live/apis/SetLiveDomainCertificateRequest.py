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


class SetLiveDomainCertificateRequest(JDCloudRequest):
    """
    设置(直播or时移)播放证书
-- 设置成功之后30分钟以内生效

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetLiveDomainCertificateRequest, self).__init__(
            '/liveDomainCertificate', 'POST', header, version)
        self.parameters = parameters


class SetLiveDomainCertificateParameters(object):

    def __init__(self, playDomain, certStatus, ):
        """
        :param playDomain: (直播or时移)播放域名
        :param certStatus: (直播or时移)播放证书状态
  on: 开启
  off: 关闭
- 当播放证书状态on(开启)时,cert和key不能为空

        """

        self.playDomain = playDomain
        self.certStatus = certStatus
        self.cert = None
        self.key = None
        self.title = None

    def setCert(self, cert):
        """
        :param cert: (Optional) (直播or时移)播放证书
- 取值: 最大支持4098
- 当播放证书状态on(开启)时,cert不能为空

        """
        self.cert = cert

    def setKey(self, key):
        """
        :param key: (Optional) (直播or时移)播放证书key
- 取值: 最大支持2048
- 当播放证书状态on(开启)时,key不能为空

        """
        self.key = key

    def setTitle(self, title):
        """
        :param title: (Optional) (直播or时移)播放证书别名
- 取值: 支持大小写字母和数字 长度最大256

        """
        self.title = title
