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


class ConfigItem(object):

    def __init__(self, configName, configValue, ):
        """
        :param configName:  configName目前只支持以下参数：
maxmemory-policy（redis 2.8和redis 4.0都支持，但配置值不相同）：内存剔除策略的最大使用内存限制
hash-max-ziplist-entries（redis 2.8和redis 4.0都支持）：用ziplist编码实现的哈希对象，ziplist中最多能存放entry个数的阈值
hash-max-ziplist-value（redis 2.8和redis 4.0都支持）：用ziplist编码实现的哈希对象，ziplist中能存放的value长度的最大值
list-max-ziplist-entries（只有redis 2.8支持）：用ziplist编码实现的列表对象，ziplist中最多能存放entry个数的阈值
list-max-ziplist-value（只有redis 2.8支持）：用ziplist编码实现的列表对象，ziplist中能存放的value长度的最大值
list-max-ziplist-size（只有redis 4.0支持）：用ziplist编码实现的列表对象，按照数据项个数或占用的字节数，限定ziplist的长度
list-compress-depth（只有redis 4.0支持）：用ziplist编码实现的列表对象，quicklist两端不被压缩的节点个数
set-max-intset-entries（redis 2.8和redis 4.0都支持）：用intset编码实现的集合对象，intset中最多能存放entry个数的阈值
zset-max-ziplist-entries（redis 2.8和redis 4.0都支持）：用ziplist编码实现的有序集合对象，ziplist中最多能存放entry个数的阈值
zset-max-ziplist-value（redis 2.8和redis 4.0都支持）：用ziplist编码实现的有序集合对象，ziplist中能存放的value长度的最大值
slowlog-log-slower-than（redis 2.8和redis 4.0都支持）：慢查询日志超时时间，单位微秒（1000000表示1秒），0表示记录所有的命令
notify-keyspace-events（只有redis 4.0支持）：事件通知

        :param configValue:  参数的配置值，默认值、参考值如下：
maxmemory-policy（redis 2.8和redis 4.0的默认值都为volatile-lru）：redis 4.0 的参考值有[volatile-lru, allkeys-lru, volatile-lfu, allkeys-lfu, volatile-random, allkeys-random, volatile-ttl, noeviction]，redis 2.8的参考值有[volatile-lru , allkeys-lru , volatile-random , allkeys-random , volatile-ttl , noeviction]
hash-max-ziplist-entries（redis 2.8和redis 4.0的默认值都为512）：[0-10000]
hash-max-ziplist-value（redis 2.8和redis 4.0的默认值都为64）：[0-10000]
list-max-ziplist-entries（redis 2.8的默认值为512，redis 4.0不支持）：[0-10000]
list-max-ziplist-value（redis 2.8的默认值为64，redis 4.0不支持）：[0-10000]
list-max-ziplist-size（redis 4.0的默认值为-2，redis 2.8不支持）：[-5-10000]
list-compress-depth（redis 4.0的默认值为0，redis 2.8不支持）：[0-10000]
set-max-intset-entries（redis 2.8和redis 4.0的默认值都为512）：[0-10000]
zset-max-ziplist-entries（redis 2.8和redis 4.0的默认值都为128）：[0-10000]
zset-max-ziplist-value（redis 2.8和redis 4.0的默认值都为64）：[0-10000]
slowlog-log-slower-than（redis 2.8和redis 4.0的默认值都为10000）：[0-10000]
notify-keyspace-events（redis 4.0的默认值为空，redis 2.8不支持）：[K , E , g , $ , l , s , h , z , x , e , A]字母的组合，区分大小写，或为空

        """

        self.configName = configName
        self.configValue = configValue
