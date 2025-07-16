[x for x in arr if x < povit]、




1. 字节公司  -

1 kafka 你们每天的吞吐量是多少？  -> topic : 120+  , 百万量级.  每天会有集中处理，（十几万条）短时间内。
2. 线程的问题， 状态转换。 线程池。  核心线程数。 cpu
3. 类加载的时候， 单例模式， 饿汉模式， 懒汉模式。
4. 云服务。
5. kubuernate nodes.  怎么部署的？
6. 查询和sql 怎么优化。
7. 架构上的问题。 怎么分层的。 怎么业务串联起来的。 怎么调用的相互。

笔试题：


2.蚂蚁国际

蚂蚁国际 --  英文。
分布式锁， 分布式事务。  英文表达还差不多。
绩效考核很重要。

难点， 举个例子。
1, 2 技术面 ， 三面是 技术+ HR.
HR - >  1. 抗压， 你怎么看待。 你会从几个角度，



kafka retention  policy  - 大于7天， 大于1G   ,  Gzip、Snappy

动态。

分布式事务。   最终一致性。

notification 幂等性， -> request message id table .

spring web security  ->  spring cloud Oauth2

物化视图和普通的视图的区别？
限流的方式有那些？

https://leetcode.cn/problems/a7VOhD/description/



以下信息需要了解一下：
1、目前薪资（月薪+年总）： (4.4万+（53+4(奖金)）)
2、期望薪资： 60+
3、看机会原因： 花旗公司集体裁员
4、到岗时间： 随时
5、出生年月以及婚姻状况： 1986-10-24， 已婚
6，籍贯和定居地: 陕西，已经定居上海
7，英语可否无障碍沟通： 是
目前的公司有内部级别吗？晋升到此职级的时间，是否带团队，几人 ， 公司的级别是VP(vice president) ， 2023年升到VP.  带两个团队（java 团队（6） 和AI 团队（7））



https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked

算法题

蚂蚁国际： 合并区间 输出数组内最高频率的数字
特斯拉： 337. 打家劫舍 III  他还给了一个拓展 ， 返回这个最大路径里面所有的值（array
字节跳动： LCR 020. 回文子串

力扣原题735 小行星碰撞,Leetcode47，和leetcode143





/Users/harry/miniforge3/envs/llm_ft/bin/python /Users/harry/PycharmProjects/algorithm_study/study_python/leecode/backtrack/permute.py
[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[1, 3, 2]
[2]
[2, 1]
[2, 1, 3]
[2, 3]
[2, 3, 1]
[3]
[3, 1]
[3, 1, 2]
[3, 2]
[3, 2, 1]
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Process finished with exit code 0

[[], [1], [1, 1], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2], [1, 2, 2], [1, 2, 3], [1, 3], [1, 3, 3], [2], [2, 2], [2, 2, 2], [2, 2, 3], [2, 3], [2, 3, 3], [3], [3, 3], [3, 3, 3]]
