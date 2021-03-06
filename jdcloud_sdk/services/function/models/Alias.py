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


class Alias(object):

    def __init__(self, aliasId=None, aliasName=None, functionName=None, description=None, version=None):
        """
        :param aliasId: (Optional) 别名Id
        :param aliasName: (Optional) 别名名称
        :param functionName: (Optional) 别名对应的函数名称
        :param description: (Optional) 别名描述信息
        :param version: (Optional) 别名对应的版本名称
        """

        self.aliasId = aliasId
        self.aliasName = aliasName
        self.functionName = functionName
        self.description = description
        self.version = version
