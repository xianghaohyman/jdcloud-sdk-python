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


class ProductProperty(object):

    def __init__(self, name, dataType, description=None, unit=None, unitName=None, min=None, max=None, step=None, length=None, enumInfo=None):
        """
        :param name:  名称, 1~30个字符，仅支持英文字母、数字、下划线“_”及中划线“-”，必须英文字母及数字开头结尾
        :param description: (Optional) 描述, 0-50个字符
        :param dataType:  数据类型，string:字符串，bool:布尔，float:单精度浮点数，double:双精度浮点数，int32:整型，enum:枚举
        :param unit: (Optional) 单位, 0-10个字符
        :param unitName: (Optional) 单位名称, 0-10个字符
        :param min: (Optional) 参数最小值(int32, float, double类型时,必填)
整型取值范围：-2的31次方 ~2的31次方-1
单精度浮点取值范围：-2的128次方+1 ~2的128次方-1,最多7位小数
双精度浮点取值范围：-2的1023次方+1 ~2的1023次方-1,最多14位小数

        :param max: (Optional) 参数最大值(int32, float, double类型时,必填)
最大值必须大于最小值
整型取值范围：-2的31次方 ~2的31次方-1
单精度浮点取值范围：-2的128次方+1 ~2的128次方-1,最多7位小数
双精度浮点取值范围：-2的1023次方+1 ~2的1023次方-1,最多14位小数

        :param step: (Optional) 参数步长(int32, float, double类型时,必填)
整型取值范围：0 ~2的31次方-1
单精度浮点取值范围：0 ~2的128次方-1,最多7位小数
双精度浮点取值范围：0~2的1023次方-1,最多14位小数

        :param length: (Optional) 参数长度(string类型特有时,必填)
取值范围:1-256之间的整数)

        :param enumInfo: (Optional) 枚举定义信息(enum、bool类型时,必填)
布尔值名称：不可为空，支持汉字、英文字母、数字。长度为1-10个字符
枚举值:为字符型，0~99。至少包括两个枚举值。输入“0”时，仅支持1位。其他数字不支持以0开头
枚举值名称：不可为空，支持汉字、英文字母、数字。长度为1-10个字符
枚举类型格式如:{10:"on",10:"off"}
布尔类型格式如:{"True":"12","False":"22"}
        """

        self.name = name
        self.description = description
        self.dataType = dataType
        self.unit = unit
        self.unitName = unitName
        self.min = min
        self.max = max
        self.step = step
        self.length = length
        self.enumInfo = enumInfo