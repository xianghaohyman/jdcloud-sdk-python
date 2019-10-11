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


class Event(object):

    def __init__(self, name=None, eventId=None, eventType=None, output=None, createdTime=None):
        """
        :param name: (Optional) 事件名称
        :param eventId: (Optional) 事件ID
        :param eventType: (Optional) 事件类型
        :param output: (Optional) 输出参数,object的key为参数名称，value为参数值
        :param createdTime: (Optional) 产生时间
        """

        self.name = name
        self.eventId = eventId
        self.eventType = eventType
        self.output = output
        self.createdTime = createdTime
