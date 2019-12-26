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


class DescribeCustomerBillByProductRequest(JDCloudRequest):
    """
    查询服务商相关pin下每个产品的消费数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCustomerBillByProductRequest, self).__init__(
            '/regions/{regionId}/accountingBill:describeCustomerBillByProduct', 'GET', header, version)
        self.parameters = parameters


class DescribeCustomerBillByProductParameters(object):

    def __init__(self, regionId, startTime, endTime, pageSize, pageIndex):
        """
        :param regionId: 
        :param startTime: 按月查询开始时间（yyyy-MM-dd）,不可跨月
        :param endTime: 按月查询结束时间（yyyy-MM-dd）,不可跨月
        :param pageSize: 每页条数,不超过100
        :param pageIndex: 第几页
        """

        self.regionId = regionId
        self.pin = None
        self.startTime = startTime
        self.endTime = endTime
        self.pageSize = pageSize
        self.pageIndex = pageIndex

    def setPin(self, pin):
        """
        :param pin: (Optional) pin
        """
        self.pin = pin

