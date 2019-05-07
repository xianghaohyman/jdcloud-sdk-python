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


class SendSingleSmsSpec(object):

    def __init__(self, appId, sign, templateId, phone, params=None):
        """
        :param appId:  应用Id
        :param sign:  短信签名名称
        :param templateId:  模板Id
        :param phone:  国内电话号码
        :param params: (Optional) 短信模板变量对应的数据值,Array格式
        """

        self.appId = appId
        self.sign = sign
        self.templateId = templateId
        self.phone = phone
        self.params = params