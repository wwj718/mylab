Date: 2013-8-09
Title: 基于Pelican和github的静态博客搭建过程
Slug: pelican
Tags:  python pelican 

前两天刚把博客搭好，如你所见，你所在的地方就是用`Pelican`搭建的    
为何使用`github`来搭建博客呢，[这里](#todo)给出了理由   
Why not [Jekyll](#todo)?    
Jekyll基于`ruby`,Pelican基于`python`，我更习惯python，如此而已   
使用Pelican之后，你只要用`markdown`格式写日志，Pelican会把markdown转换成`html`的格式，之后push到github pages上, 就可以看到你写的日志了，就是说你的所有工作就是用markdown写作，是不是很惬意^_^   
Pelican 的一些主要`特性`：

*  Python实现，开放源码
*  输出静态页面，方便托管
*  支持主题，采用Jajin2模板引擎
*  支持代码语法高亮
*  支持reStructuredText、Markdown、AsciiDoc格式
*  支持Disqus评论
*  支持Atom和RSS输出


闲话不说，进入主题   
我假设你是初来乍到的小白.（我也是小白啦～）虽说是小白,搭建这种geek类博客并没有你想象的费劲。just do it     
首先，你得把git给入门了，入门简单，要掌握的命令不多，这是[git基本教程](#todo)（虽说git的学习曲线很陡峭，基本用法还是很容易的，don't worry about it） 
我假设你掌握了基本的git命令，接着我们可以正式开始了 
##安装linux系统
as a geek(或者渴望成为geek的小白）你还抱着win7不放么，还舍不得那熟悉的蓝屏么，还舍不得莫名其妙的报错么,果断抛弃娇气的windows，投入linux的怀抱吧。俺使用的发行版是Ubuntu12.04.一直很稳定且顺心    
你要执意使用window，之后可能在环境配置上得费些功夫，其他基本一样。
本文的环境是Ubuntu12.04。

##安装Pelican
    pip install pelican
   
####使用Markdown来写文章的话，还需要安装Markdown库 
    pip install Markdown

####创建blog目录：

    mkdir myblog
    cd myblog

####创建一个博客：(在当前目录下，即myblog)
    pelican-quickstart
按照提示设置，可按默认的设置，之后可在pelicanconf.py文件中修改设置。

以下是生成的目录结构：

    myblog/     
    ├── content              # 存放输入的源文件  
    ├── output               # 生成的输出文件  
    ├── develop_server.sh    # 方便开启测试服务器    
    ├── Makefile             # 方便管理博客的Makefile  
    ├── pelicanconf.py       # 主配置文件    
    └── publishconf.py       # 发布时使用的配置文件   

####写一篇文章
以mardown格式举例，具体可以去看pelican的文档. 进入content目录，创建一个文件，写入博客内容：

    Date: 2013-8-9 #日期

    Title: test ＃标题

    Tags: python pelican github #标签

    Category: python #分类

其中Date和Title是必须的，其它的可以不写    
如果该文件位于content目录中某个子目录中时，如./content/python，那pelican就把这篇文章分类为子目录名python

####生成html

    make html
你将看到output文件夹里多了×××.html文件
在myblog所在的地方新建一个myblog_for_github（名字随意）,把output里的文件复制到里面。   
为何呢，下文解释
##在github上创建GitHub Pages
新建一个Repository，Repository名字为yourname.github.com，yourname是您的用户ID。

创建成功以后，便可以把生成的页面push到github。

    cd myblog_for_github
    git init
    git add .
    git commit -m "first commit"
    git remote add origin https://github.com/xxx/xxx.github.io.git
    git push -u origin master

现在可以通过 xxx.github.io 或者 xxx.github.com 来访问您的博客了。

##修改以及更新博客
看了几篇资料，里面似乎都没有谈到后续继续写博客的问题，当然这不属于搭建的问题  
顺带也提一下吧，做个备忘。   
当我们隔了几天继续写博客时，把写好的×××.md文件放到content文件夹里输入：  
    make html
之所以要把内容复制到myblog_for_github里再提交，是因为每次执行 
    make html
output里的文件会被覆盖，不能在这里git init，否则仓库会被删了   
至于增删改已经提交的博客的内容基本是git的任务，也就是本教程之初让你去入门git的原因    
会用到的一些指令：

    git rm ×××.html    //删除代码库中文件
    git add . 
    git commit -m "some message"
    git push -u origin master

##域名绑定
在repo的根目录下面，新建一个名为CNAME的文本文件，里面写入你要绑定的域名，比如顶级域名 example.com 或者二级域名 xxx.example.com。


遇到问题请谷歌,或者查看官方文档

参考资料:

1.  [用pelican在github上创建博客极简教程](#todo)
2.  [Pelican官方文档](http://readthedocs.org/docs/pelican/en/2.8/)
3.  [用 Pelican 和 GitHub Pages 搭建免费的个人博客](#todo)
