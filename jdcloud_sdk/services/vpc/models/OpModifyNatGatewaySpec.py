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


class OpModifyNatGatewaySpec(object):

    def __init__(self, bandwidthMbps, userPin, ):
        """
        :param bandwidthMbps:  公网IP的限速（单位：Mbps），取值范围为[1-4000]
        :param userPin:  资源所属的用户pin
        """

        self.bandwidthMbps = bandwidthMbps
        self.userPin = userPin
