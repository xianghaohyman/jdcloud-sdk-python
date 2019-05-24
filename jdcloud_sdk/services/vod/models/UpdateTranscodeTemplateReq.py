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


class UpdateTranscodeTemplateReq(object):

    def __init__(self, id=None, name=None, video=None, audio=None, encapsulation=None, definition=None):
        """
        :param id: (Optional) 模板ID
        :param name: (Optional) 模板名称
        :param video: (Optional) 视频参数
        :param audio: (Optional) 音频参数
        :param encapsulation: (Optional) 封装配置
        :param definition: (Optional) 清晰度规格
        """

        self.id = id
        self.name = name
        self.video = video
        self.audio = audio
        self.encapsulation = encapsulation
        self.definition = definition
