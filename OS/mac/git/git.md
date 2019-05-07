git回滚到任意版本

先显示提交的log

$ git log -3
commit 4dc08bb8996a6ee02f
Author: Mark <xxx@xx.com>
Date:   Wed Sep 7 08:08:53 2016 +0800

    xxxxx

commit 9cac9ba76574da2167
Author: xxx<xx@qq.com>
Date:   Tue Sep 6 22:18:59 2016 +0800

    improved the requst

commit e377f60e28c8b84158
Author: xxx<xxx@qq.com>
Date:   Tue Sep 6 14:42:44 2016 +0800

    changed the password from empty to max123
回滚到指定的版本

git reset --hard e377f60e28c8b84158
强制提交

git push -f origin master



Git——如何将本地项目提交至远程仓库(第一次)
1.（先进入项目文件夹）通过命令 git init 把这个目录变成git可以管理的仓库。

git init
 
2.把文件添加到版本库中，使用命令 git add .添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文件夹下的所有文件(夹)。

git add .
 

3.commit到主分支

git commit -m "描述" 
 

4.登录github，把本地仓库提交至远程仓库。

接下来你要做的就是复制那个地址，然后你将本地仓库个远程仓库连接起来。

git remote add origin git@github.com:Garretming/blog.git  
 

5.进行第一次提交

git push -u origin master  
 

ps: windows系统中使用git时报错“warning: LF will be replaced by CRLF”解决方案：

复制代码
复制代码
$ rm -rf .git  // 删除.git  
$ git config --global core.autocrlf false  //禁用自动转换 

//然后重新执行

$ git init    
$ git add . 
复制代码
复制代码
 

rm -rf .git慎用！！！！原因详见：https://www.zhihu.com/question/29438735 不小心敲了rm -rf后反应是怎样的？