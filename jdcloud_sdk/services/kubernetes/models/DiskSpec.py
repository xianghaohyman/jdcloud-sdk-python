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


class DiskSpec(object):

    def __init__(self, systemDiskCategory=None, systemDiskSize=None, systemDiskType=None, systemDiskIops=None):
        """
        :param systemDiskCategory: (Optional) 磁盘类型，取值为cloud、local，默认为cloud
        :param systemDiskSize: (Optional) 云盘系统盘的大小 单位(GB)
        :param systemDiskType: (Optional) 云盘系统盘的类型，支持 hdd.std1,ssd.gp1,ssd.io1
        :param systemDiskIops: (Optional) 云盘 iops，仅限 ssd.io1 类型云盘有效
        """

        self.systemDiskCategory = systemDiskCategory
        self.systemDiskSize = systemDiskSize
        self.systemDiskType = systemDiskType
        self.systemDiskIops = systemDiskIops