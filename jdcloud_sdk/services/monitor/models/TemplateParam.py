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


class TemplateParam(object):

    def __init__(self, name, params, tags, templateAddr, thumbnailAddr, description=None):
        """
        :param description: (Optional) 描述
        :param name:  名称
        :param params:  模板参数信息,必须有数据源信息
        :param tags:  模板标签, map[string]string, 必须有数据源的标签,比如"datasourceType":"cloudmonitor"
        :param templateAddr:  模板oss地址
        :param thumbnailAddr:  模板缩略图oss地址
        """

        self.description = description
        self.name = name
        self.params = params
        self.tags = tags
        self.templateAddr = templateAddr
        self.thumbnailAddr = thumbnailAddr