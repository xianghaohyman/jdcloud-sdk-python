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


class CertQuotaLimitDetail(object):

    def __init__(self, id=None, account=None, freeUploadCertCount=None, freeDVSingleCount=None):
        """
        :param id: (Optional) 主键ID
        :param account: (Optional) 用户名称(用户pin)
        :param freeUploadCertCount: (Optional) 基于pin的最大可上传证书配额数
        :param freeDVSingleCount: (Optional) 基于pin的最大可购买免费证书配额数
        """

        self.id = id
        self.account = account
        self.freeUploadCertCount = freeUploadCertCount
        self.freeDVSingleCount = freeDVSingleCount
