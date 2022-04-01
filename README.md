# pagerank
实验二：PageRank算法实现

 

​	为减轻同学作业压力，科学评价完成效果，请同学们先阅读本文档，再完成实验。实验完成后，依次回答本文档中的所有问题并将修改后的本文档提交即可。

​	你需要且仅需要在网络学堂提交修改后的本文档。

 

一、 实现PageRank算法，通过OJ测试：

l 登录OJ的账号密码请在网络学堂“已批改的作业”查收

l OJ网址为oj.thusaac.com

l 我们的相关文件可以在网络学堂上下载

n wiki.graph为用于计算的结构图

n wiki.pagerank为![img](file:////private/var/folders/l9/26smcc0n28v511jmpwdz3s5w0000gn/T/com.kingsoft.wpsoffice.mac/wps-yangwenyu/ksohtml/wpsf6MVK7.jpg)时的输出文件，以供参考

n node.map.gbk/node.map.utf8为节点编号和词条的映射（分别为gbk和utf-8格式）

l 在这个实验中，我们取![img](file:////private/var/folders/l9/26smcc0n28v511jmpwdz3s5w0000gn/T/com.kingsoft.wpsoffice.mac/wps-yangwenyu/ksohtml/wpsLBsPeA.jpg)

l 迭代到收敛（请思考或实验要迭代多少轮）

l 如果你的输出和标准输出的绝对误差在![img](file:////private/var/folders/l9/26smcc0n28v511jmpwdz3s5w0000gn/T/com.kingsoft.wpsoffice.mac/wps-yangwenyu/ksohtml/wpsfbXSeG.jpg)以内，我们就认为你的答案是正确的（因此请至少输出10位小数）

l 输入格式：

n 输入数据包含1109153行，每行格式详见PPT第54页，head和node均为![img](file:////private/var/folders/l9/26smcc0n28v511jmpwdz3s5w0000gn/T/com.kingsoft.wpsoffice.mac/wps-yangwenyu/ksohtml/wpsTEG5c3.jpg)以内的正整数

l 输出格式

n 输出若干行，对于输入数据中出现过（不管是在head出现过还是在node出现过）的节点，输出一行，包含一个整数和一个浮点数，整数为节点编号，浮点数为它的PageRank。按照节点编号从小到大依次输出

l 注意到OJ运行代码时有如下限制：

n 程序运行时间：60s

n 程序运行内存（以最大驻留集计算）：2GB

n 代码长度限制：64kb

l 输入的图中有一些corner case，例如：

n 某一行的内容为：“A:”，即只描述了一个节点，没有描述它的任何出边

n 某两行的内容为：“A:B,C”，“A:B,D”，即多次描述了一个节点的出边，此时应当认为A的出边有“B,B，C,D”

n 图中可能存在自环，自环应当视为出边

n 图中可能存在重边，重边应当视为多条出边

*l* **请在这里贴上通过OJ测试的截图**

*l* **我们会对代码进行查重**

*l* **如果你想用OJ上没有配置的语言完成本题，请与助教联系**

二、 实验报告

l 请分析在迭代过程中，为什么PageRank值的和始终为1

 

l 语料入链接数和出链接数分布情况分布图：

 

l 对入链接和出链接数分布进行分析（100字以内）

 

l PageRank结果分布图：

 

l 分析（100字以内）

 

l PageRank得分与入链接的关联分析（100字以内，可作图）

 

l PageRank得分与相应条目语义内容分析（取不超过5个有代表性的词分析，400字以内）

 

l 其他你认为值得描述的内容（200字以内）

 

 

 

 
