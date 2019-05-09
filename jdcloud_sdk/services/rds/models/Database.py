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


class Database(object):

    def __init__(self, dbName=None, dbStatus=None, characterSetName=None, createTime=None, accessPrivilege=None):
        """
        :param dbName: (Optional) 数据库名称，具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param dbStatus: (Optional) 数据库状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- **MySQL：不支持，不返回该字段**<br>- **SQL Server：返回该字段**
        :param characterSetName: (Optional) 字符集，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param createTime: (Optional) 数据库创建时间，格式YYYY-MM-DD HH:mm:ss<br>- 仅支持SQL Server
        :param accessPrivilege: (Optional) 该数据库相关账户权限列表
        """

        self.dbName = dbName
        self.dbStatus = dbStatus
        self.characterSetName = characterSetName
        self.createTime = createTime
        self.accessPrivilege = accessPrivilege
