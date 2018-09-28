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


class ImageDetail(object):

    def __init__(self, registryName=None, repositoryName=None, imageDigest=None, imageManifest=None, imagePushedAt=None, imageSizeMB=None, imageTags=None, lastPullAt=None, totalPullTimes=None):
        """
        :param registryName: (Optional) image registry 表示镜像的注册表归属
        :param repositoryName: (Optional) image repository表示镜像的仓库归属
        :param imageDigest: (Optional) image manifest的sha256摘要
        :param imageManifest: (Optional) 镜像的Manifest
        :param imagePushedAt: (Optional) 当前image被push到repository的时间
        :param imageSizeMB: (Optional) image在repository中的大小。从Docker 1.9之后的版本, Docker client会压缩镜像层数据再push到V2版本的Docker registry。
docker image命令显示的是解压后的镜像大小，因此会比DescribeImages接口返回的镜像大小会大很多。      

        :param imageTags: (Optional) 镜像关联的所有Tag
        :param lastPullAt: (Optional) 最近pull的时间
        :param totalPullTimes: (Optional) 镜像被拉取次数
        """

        self.registryName = registryName
        self.repositoryName = repositoryName
        self.imageDigest = imageDigest
        self.imageManifest = imageManifest
        self.imagePushedAt = imagePushedAt
        self.imageSizeMB = imageSizeMB
        self.imageTags = imageTags
        self.lastPullAt = lastPullAt
        self.totalPullTimes = totalPullTimes