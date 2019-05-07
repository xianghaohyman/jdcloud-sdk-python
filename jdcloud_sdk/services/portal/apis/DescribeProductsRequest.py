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


class DescribeProductsRequest(JDCloudRequest):
    """
    产品页列表查询接口

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeProductsRequest, self).__init__(
            '/regions/{regionId}/products', 'GET', header, version)
        self.parameters = parameters


class DescribeProductsParameters(object):

    def __init__(self, regionId, lang, ak):
        """
        :param regionId: Region ID （cn-north-1：华北-北京）
        :param lang: 语言类型；中文cn；英文en；
        :param ak: 外部使用ak；
        """

        self.regionId = regionId
        self.lang = lang
        self.ak = ak
