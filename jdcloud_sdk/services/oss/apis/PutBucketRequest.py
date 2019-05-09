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


class PutBucketRequest(JDCloudRequest):
    """
    创建bucket

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(PutBucketRequest, self).__init__(
            '/regions/{regionId}/buckets/{bucketname}', 'PUT', header, version)
        self.parameters = parameters


class PutBucketParameters(object):

    def __init__(self, regionId, bucketname, ):
        """
        :param regionId: Region ID，例如：cn-north-1
        :param bucketname: bucket名字，例如：test-bucket
        """

        self.regionId = regionId
        self.bucketname = bucketname

