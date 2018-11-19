====================================
Python 官方文档简体中文翻译计划
====================================

这是 Python 3.7 官方文档的简体中文（zh_CN）翻译

翻译之前，请务必详读并同意\ `授权与 License`_\ 。参与方式请参考\ `参与翻译`_\ 。

您可以在 https://docs.python.org/zh-cn/3.7/ 浏览目前的翻译成果。

想问问题、认识翻译同好，欢迎联系 `songww <mailto:sww4718168@gmail.com>`_ 加入微信群。

.. contents:: **目录**

授权与 License
=================

以下为 Documentation Contribution Agreement，说明翻译贡献协议，请在贡献之前务必详读以下内容。

Documentation Contribution Agreement
------------------------------------

NOTE REGARDING THE LICENSE FOR TRANSLATIONS: Python's documentation is
maintained using a global network of volunteers. By posting this
project on Transifex, GitHub, and other public places, and inviting
you to participate, we are proposing an agreement that you will
provide your improvements to Python's documentation or the translation
of Python's documentation for the PSF's use under the CC0 license
(available at
https://creativecommons.org/publicdomain/zero/1.0/legalcode). In
return, you may publicly claim credit for the portion of the
translation you contributed and if your translation is accepted by the
PSF, you may (but are not required to) submit a patch including an
appropriate annotation in the Misc/ACKS or TRANSLATORS file. Although
nothing in this Documentation Contribution Agreement obligates the PSF
to incorporate your textual contribution, your participation in the
Python community is welcomed and appreciated.

You signify acceptance of this agreement by submitting your work to
the PSF  for inclusion in the documentation.

参与翻译
=================

1. 在transifex创建帐号，并申请加入 Transifex Chinese(China) Team `https://www.transifex.com/python-docs/public`_ 。

2. 选择需要翻译的 Project，当前以翻译 Python 最新版为先，https://www.transifex.com/python-doc/python-newest/dashboard/

3. 选择需要翻译的文件 https://www.transifex.com/python-doc/python-newest/language/zh_CN/

当前的目标为完成 **Tutorial** 的翻译，因此以 ``tutorial--`` 开头的所有
文档都最高优先级翻译的内容。您也可以帮忙校对已经翻译过的内容。

排版要求
=================

空格
-----------------

中英文之间需要增加空格
^^^^^^^^^^^^^^^^^
| 正确：

  - 在 LeanCloud 上，数据存储是围绕 AVObject 进行的。
  - 每个 AVObject 都包含了与 JSON 兼容的 key-value 对应的数据。
  - 数据是 schema-free 的，你不需要在每个 AVObject 上提前指定存在哪些键，只要直接设定对应的 key-value 即可。

| 错误：

  - 在LeanCloud上，数据存储是围绕AVObject进行的。
  - 在 LeanCloud上，数据存储是围绕AVObject 进行的。

| 例外：

  - “豆瓣FM”等产品名词，按照官方所定义的格式书写。

中文与数字之间需要增加空格
^^^^^^^^^^^^^^^^^

| 正确：

  - 今天出去买菜花了 5000 元。

| 错误：

  - 今天出去买菜花了 5000元。
  - 今天出去买菜花了5000元。

数字与单位之间需要增加空格
^^^^^^^^^^^^^^^^^

| 正确：

  - 我家的光纤入户宽带有 10 Gbps，SSD 一共有 20 TB。

| 例外，度／百分比与数字之间不需要增加空格：

  - 今天的温度高达 233° 。
  - 新 MacBook Pro 的 CPU 有 15% 性能提升。

| 错误：

  - 我家的光纤入户宽带有 10Gbps，SSD 一共有 10TB。
  - 今天是 233 ° 的高温。
  - 新 MacBook Pro 有 15 % 的 CPU 性能提升。

全角标点与其他字符之间不加空格
^^^^^^^^^^^^^^^^^

| 正确：

  - 刚刚买了一部 iPhone，好开心！

| 错误：

  - 刚刚买了一部 iPhone ，好开心！

标点符号
-----------------

不重复使用标点符号
^^^^^^^^^^^^^^^^^

| 正确：

  - 德国队竟然战胜了巴西队！
  - 她竟然对你说“喵”？

| 错误：

  - 德国队竟然战胜了巴西队！！
  - 她竟然对你说「喵」？？！！

破折号前后需要增加一个空格
^^^^^^^^^^^^^^^^^

| 正确：

  - 你好，我是破折号 —— 一个不苟言笑的符号。

| 错误：

  - 你好，我是破折号——一个不苟言笑的符号。

半角逗号
^^^^^^^^^^^^^^^^^

  - ``,`` 可能对应逗号或者顿号。

半角句号
^^^^^^^^^^^^^^^^^

  - ``.`` 可能对应句号、分号或者逗号(分句)。

连字符
^^^^^^^^^^^^^^^^^

  - ``-`` 若为连字之用,可不译（前后均为 CJK 的话），或保留原样（译文中前后有至少一个西文的话）。

  - 有时你会注意到它被误用作连接号 en-dash – 的用途，那也要反应过来并用中文连接号—译。
  就像 Ubuntu-Debian Distro Family，翻译成“乌版图—大便发行版家族”（我后悔用 Debian 举例了）。

省略号
^^^^^^^^^^^^^^^^^

   - ``...`` 省略号应保持不变。

冒号
^^^^^^^^^^^^^^^^^

  - ``:`` 应翻译为 ``：`` ,而作为分隔符使用的 ``23:59`` 仍然应使用半角冒号。


全角和半角
-----------------

不明白什么是全角（全形）与半角（半形）符号？请查看维基百科词条 `全角和半角`_\ 。

.. 全角和半角: http://zh.wikipedia.org/wiki/%E5%85%A8%E5%BD%A2%E5%92%8C%E5%8D%8A%E5%BD%A2


使用全角中文标点
^^^^^^^^^^^^^^^^^

| 正确：

  - 嗨！你知道嘛？今天前台的小妹跟我说“喵”了哎！
  - 核磁共振成像（NMRI）是什么原理都不知道？JFGI！

| 错误：

  - 嗨! 你知道嘛? 今天前台的小妹跟我说 "喵" 了哎!
  - 核磁共振成像(NMRI)是什么原理都不知道?JFGI!

数字使用半角字符
^^^^^^^^^^^^^^^^^

| 正确：

  - 这件蛋糕只卖 1000 元。

| 错误：

  - 这件蛋糕只卖 １０００ 元。


遇到完整的英文整句、特殊名词，其內容使用半角标点
^^^^^^^^^^^^^^^^^

| 正确：

  - 乔布斯那句话是怎么说的？“Stay hungry, stay foolish.”
  - 推荐你阅读《Hackers & Painters: Big Ideas from the Computer Age》，非常的有趣。

| 错误：

  - 乔布斯那句话是怎么说的？“Stay hungry，stay foolish。”
  - 推荐你阅读《Hackers＆Painters：Big Ideas from the Computer Age》，非常的有趣。


名词
-----------------

专有名词使用正确的大小写
^^^^^^^^^^^^^^^^^

| 正确：

  - 使用 GitHub 登录
  - 我们的客户有 GitHub、Foursquare、Microsoft Corporation、Google、Facebook, Inc.。

| 错误：

  - 使用 github 登录
  - 使用 GITHUB 登录
  - 使用 Github 登录
  - 我们的客户有 github、foursquare、microsoft corporation、google、facebook, inc.。
  - 我们的客户有 GITHUB、FOURSQUARE、MICROSOFT CORPORATION、GOOGLE、FACEBOOK, INC.。

不要使用不地道的缩写
^^^^^^^^^^^^^^^^^

| 正确：

  - 我们需要一位熟悉 JavaScript、HTML5，至少理解一种框架（如 Backbone.js、AngularJS、React 等）的前端开发者。

| 错误：

  - 我们需要一位熟悉 Js、h5，至少理解一种框架（如 backbone、angular、RJS 等）的 FED。


排版
-----------------

斜体文字使用加粗样式代替
^^^^^^^^^^^^^^^^^

| 正确：

  - **斜体本身是为西文文字所设计，为了保持良好的阅读效果，在中文排版时不应出现斜体，因此统一使用加粗样式代替。**

| 错误：

  - *斜体本身是为西文文字所设计，为了保持良好的阅读效果，在中文排版时不应出现斜体，因此统一使用加粗样式代替。*


RST 标记
-----------------

Python docs 使用 reStructuredText 标记语言编写，因此我们在翻译过程中会遇到很多RST标记。
大部分标记两侧都需要添加空格，不添加空格会导致编译失败。
部分编译后的内容有空格会变的古怪，可用 ``\`` 对空格转义，使其变为编译后不可见，下面有示例


链接
^^^^^^^^^^^^^^^^^

- 链接到外部站点：

  例如：

  .. code-block:: rst

    These documents are generated from `reStructuredText`_ sources by `Sphinx`_, a document processor specifically written for the Python documentation.

  翻译为：

  .. code-block:: rst

    这些文档生成自 `reStructuredText`_ 原文档，由 `Sphinx`_ 一个专门为 Python 文档写的文档生成器创建。

  其中 ```reStructuredText`_`` 和 ```Sphinx`_`` 是指向外部的超链接标记，不应该翻译，且标记两侧需添加空格，不然会编译失败。

- 链接到源码：

  例如：

  .. code-block:: rst

    See :source:`Misc/ACKS` in the Python source distribution for a partial list of contributors.

  翻译为：

  .. code-block:: rst

    部分贡献者可在 Python 源码中的 :source:`Misc/ACKS` 文件中找到。

  ``:source:`Misc/ACKS``` 是指向源码文件的链接。亦不应翻译且应保留两侧空格。

- 内联标记：

  例如：

  .. code-block:: rst

    `How to Report Bugs Effectively <https://www.chiark.greenend.org.uk/~sgtatham/bugs.html>`_

  翻译为：

  .. code-block:: rst

    `如何高效的报告 Bugs <https://www.chiark.greenend.org.uk/~sgtatham/bugs.html>`_

  其中 ``How to Report Bugs Effectively`` 是显示文字，可以根据内容判断是否需要翻译。

  如果翻译，注意标记两侧同样需要添加空格，但空格可以使用 ``\`` 转义，避免编译后产生多余的空白符。

  如\ `如何高效的报告 Bugs <https://www.chiark.greenend.org.uk/~sgtatham/bugs.html>`_\ 。

- 链接到其他页面：

  例如：

  .. code-block:: rst

    For a guide to installing other Python projects, refer to the :ref:`installation guide`.

  翻译为：

  .. code-block:: rst

    有关安装其他 Python 项目的指南，参阅 :ref:`installation guide` 。

  其中 ``:ref:`installation guide``` 会编译为指向 Python docs 安装指南的链接。请勿翻译。

  例如：

  .. code-block:: rst

    :mod:`distutils` is the original build and distribution system first added to the Python standard library in 1998.

  其中 ``:mod:`distutils``` 会编译为指向 distutils 模块文档的链接，请勿翻译。


代码标记
^^^^^^^^^^^^^^^^^

  ````if True:```` 这样的标记是等宽标记，一般是代码，请勿翻译。



术语表
=================

为了保持翻译的统一，我们整理了一份术语列表，如果您有不同意的地方，欢迎通过 issue 或 Pull Request 一起讨论。

============= ==================
原文          翻译
============= ==================
argument      参数、实参
attribute     属性
boolean       boolean（布尔）
class         class（类、类型）
contributor   贡献者
deprecated    已弃用
dictionary    dictionary（字典）
dict          dict（字典）
element       元素
exception     异常
expression    表达式
float         浮点数
function      函数
import        import（导入）
index         索引
instance      实例
int           int（整型）
interpreter   解释器
iterate       迭代
iterater      迭代器
list          list（列表）
loop          循环
method        method（方法）
module        module（模块）
object        object（对象）
operand       operand
operator      操作符
parameter     形参
prompt        prompt
return        返回
set           set（集合）
statement     statement
type          类型
============= ==================


报告问题
=================

提交 Issue_\ 或者加入微信群。

.. _Issue: https://github.com/python/python-docs-zh-cn/issues

另外可以直接联系翻译的 coordinator `Shengjing Zhu <https://github.com/zhsj>`_ 和 `Xiang Zhang <https://github.com/zhangyangyu>`_\ 。
