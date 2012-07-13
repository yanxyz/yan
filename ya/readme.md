要求Python 2.7.x。
仅在win7下测试过。

使用前先编辑config.py，修改配置。
使用时拖动文件到相应py文件上。

这套工具待开发为GUI。

yuicompressor.py
--------------

利用yuicompressor压缩js与css文件。

需要java>=1.6，命令提示符下可运行java。

生成压缩后的文件名，规则为：

1. 文件名有 .source 时: filename.source.js -> filename.js
2. 其它情况：filename.js -> filename-min.js

Native2ascii.py
------------

需要jdk>=1.6，命令提示符下可运行Native2ascii.exe。

当js、css文件的编码与页面编码不一致时，非 ascii 字符会导致乱码，
将代码转为ascii可避免这种情况。


url.py
-----

在默认浏览器中打开本地服务器上的文件。

output.py
--------

保存本地服务器上动态文件的输出，即html文件。
简单的整理了缩进。要求源文件中html标签对称，如

	<p>
	<span>It's a test</span>
	</p>

不能这样：

	<p>
	<span>It's a test</span></p>

	<p><span>It's a test</span>
	</p>

CssGagaSlice.py
------------

事先安装好[PIL模块][]。

仿[CssGaga][]的SliceToCode功能，将生成的css代码保存保存到css文件中，满足保存到css文件的需求，同时没有图片压缩过程相对快一点。

CssGagaSprite.py
------------

[CssGaga][]合成sprite后，有许多重复的background-image，这样冗余下来的代码还是比较可观的。尝试合并，对于场景复杂的情况还待测试。


[PIL模块]:http://www.pythonware.com/products/pil/
[CssGaga]:http://www.99css.com/archives/542	
