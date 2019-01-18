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


class TaskInfo(object):

    def __init__(self, beginTime=None, endTime=None, taskStatus=None, taskResult=None, lastCode=None, taskLastInfo=None, resourceIDs=None, msg=None):
        """
        :param beginTime: (Optional) 任务执行开始时间
        :param endTime: (Optional) 任务执行结束时间
        :param taskStatus: (Optional) 任务执行状态：running、finished
        :param taskResult: (Optional) 任务执行结果：done、error、nochange
        :param lastCode: (Optional) 任务执行最后编码:
CREATEING_RESOURCE_INFO->未完成:正在构建目标资源信息
CREATE_RESOURCE_INFO_ERROR->失败完成:目标资源描述信息创建失败！
CREATE_RESOURCE_INFO_SUCCESS->未完成:目标资源描述信息创建成功！开始初始化构建程序
PROGRAM_INITING->未完成:正在初始化构建程序
PROGRAM_INIT_ERROR->失败完成:构建程序初始化失败！
PROGRAM_INIT_SUCCESS->未完成:构建程序初始化成功！开始分析本次构建任务
TASK_PLAN_ERROR->失败完成:构建分析发生错误！
TASK_PLAN_NOCHANGE->完成:本次构建无可执行操作
TASK_PLAN_SUCCESS->未完成:分析完成！开始执行资源构建
TASK_RUN_FAILED->失败完成:资源构建任务执行失败！
TASK_RUN_NOCHANGE->完成:本次构建未执行任何操作
TASK_RUN_SUCCESS->完成:资源构建任务执行完毕！
        :param taskLastInfo: (Optional) 任务执行之后编码描述
        :param resourceIDs: (Optional) 任务执行成功后返回的ID列表
        :param msg: (Optional) 任务执行日志信息
        """

        self.beginTime = beginTime
        self.endTime = endTime
        self.taskStatus = taskStatus
        self.taskResult = taskResult
        self.lastCode = lastCode
        self.taskLastInfo = taskLastInfo
        self.resourceIDs = resourceIDs
        self.msg = msg