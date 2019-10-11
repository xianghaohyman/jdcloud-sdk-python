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


class Rules(object):

    def __init__(self, ruleId=None, ruleType=None, ruleInfo=None, jcqInfo=None):
        """
        :param ruleId: (Optional) 规则编号
        :param ruleType: (Optional) 0-正常规则，1-异常规则
        :param ruleInfo: (Optional) 用户填写的规则信息
        :param jcqInfo: (Optional) 用户规则映射的jcq信息
        """

        self.ruleId = ruleId
        self.ruleType = ruleType
        self.ruleInfo = ruleInfo
        self.jcqInfo = jcqInfo
