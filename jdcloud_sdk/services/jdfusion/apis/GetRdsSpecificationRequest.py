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


class GetRdsSpecificationRequest(JDCloudRequest):
    """
    根据数据库类型，取得RDS实例的规格
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetRdsSpecificationRequest, self).__init__(
            '/regions/{regionId}/rds_specification/{engine}', 'GET', header, version)
        self.parameters = parameters


class GetRdsSpecificationParameters(object):

    def __init__(self, regionId, engine, ):
        """
        :param regionId: 地域ID
        :param engine: RDS数据库引擎，目前只支持mysql
        """

        self.regionId = regionId
        self.engine = engine

