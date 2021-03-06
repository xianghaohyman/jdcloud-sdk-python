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


class QueryBillSummaryRequest(JDCloudRequest):
    """
    查询账单资源汇总数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryBillSummaryRequest, self).__init__(
            '/regions/{regionId}/billSummary:list', 'POST', header, version)
        self.parameters = parameters


class QueryBillSummaryParameters(object):

    def __init__(self, regionId, startTime, endTime, ):
        """
        :param regionId: Region ID
        :param startTime: 计费开始时间
        :param endTime: 计费结束时间
        """

        self.regionId = regionId
        self.startTime = startTime
        self.endTime = endTime
        self.appCode = None
        self.serviceCode = None
        self.resourceIds = None
        self.tags = None
        self.pageIndex = None
        self.pageSize = None

    def setAppCode(self, appCode):
        """
        :param appCode: (Optional) 产品线代码
        """
        self.appCode = appCode

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 产品代码
        """
        self.serviceCode = serviceCode

    def setResourceIds(self, resourceIds):
        """
        :param resourceIds: (Optional) 资源单id列表
        """
        self.resourceIds = resourceIds

    def setTags(self, tags):
        """
        :param tags: (Optional) 标签
        """
        self.tags = tags

    def setPageIndex(self, pageIndex):
        """
        :param pageIndex: (Optional) pageIndex
        """
        self.pageIndex = pageIndex

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) pageSize
        """
        self.pageSize = pageSize

