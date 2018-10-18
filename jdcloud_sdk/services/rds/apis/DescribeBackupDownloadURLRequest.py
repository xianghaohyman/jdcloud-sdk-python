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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeBackupDownloadURLRequest(JDCloudRequest):
    """
    获取整个备份或备份中单个文件的下载链接。<br>- 当输入参数中有文件名时，获取该文件的下载链接。<br>- 输入参数中无文件名时，获取整个备份的下载链接。<br>由于备份机制的差异，使用该接口下载备份时，SQL Server必须输入文件名，每个文件逐一下载，不支持下载整个备份。SQL Server备份中的文件名（不包括后缀）即为备份的数据库名。例如文件名为my_test_db.bak，表示该文件是my_test_db数据库的备份。<br>MySQL可下载整个备份集，但不支持单个文件的下载。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeBackupDownloadURLRequest, self).__init__(
            '/regions/{regionId}/backups/{backupId}:describeBackupDownloadURL', 'GET', header, version)
        self.parameters = parameters


class DescribeBackupDownloadURLParameters(object):

    def __init__(self, regionId, backupId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param backupId: 备份ID
        """

        self.regionId = regionId
        self.backupId = backupId
        self.fileName = None
        self.urlExpirationSecond = None

    def setFileName(self, fileName):
        """
        :param fileName: (Optional) 文件名称<br>- MySQL：不支持该参数<br>- SQL Server：必须输入该参数，指定该备份中需要获取下载链接的文件名称。备份中的文件名（不包括后缀）即为备份的数据库名。例如文件名为my_test_db.bak，表示该文件是my_test_db数据库的备份
        """
        self.fileName = fileName

    def setUrlExpirationSecond(self, urlExpirationSecond):
        """
        :param urlExpirationSecond: (Optional) 指定下载链接的过期时间，单位秒,缺省为86400秒，即24小时。<br>- MySQL：不支持该参数，只能是默认值<br>- SQL Server：支持
        """
        self.urlExpirationSecond = urlExpirationSecond

