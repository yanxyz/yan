要求Python 2.7.x。
仅在win7下测试过。

使用前先编辑config.py，修改配置。
使用时拖动文件到相应py文件上。

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

CssGagaAssit.py
------------

事先安装好[PIL模块][]。

[CssGaga][]是有这个功能的，拖动slice图片生成css代码，不过似乎有生成spirit的过程。这个脚本可将生成的css代码保存保存到css文件中，在需要多个spirit时相对方便那么一点点。

url.py
-----

在默认浏览器中打开本地服务器上的文件。

output.py
--------

保存本地服务器上动态文件的输出，即html文件。
简单的整理了缩进。要示源文件中html标签对称，如

	<p>
	<span>It's a test</span>
	</p>

不能这样：

	<p>
	<span>It's a test</span></p>

	<p><span>It's a test</span>
	</p>

[PIL模块]:http://www.pythonware.com/products/pil/
[CssGaga]:http://www.99css.com/archives/542	
