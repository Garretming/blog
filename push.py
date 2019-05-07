#!/usr/bin/evn python3
#coding=utf-8
#用于提交改动
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    message = sys.argv[1]
    if message == None:
        print('not message')
        sys.exit()
    print(sys.argv[1])
    os.system('git add -A') #所有变化提交到暂存区
    # os.system('git stash') #保存当前工作进度，会把暂存区和工作区的改动保存起来。-但没有提交到本地仓库
    os.system('git fetch origin master')#//从远程的origin的master主分支上获取最新版本到origin/master分支上
    os.system('git log -p master..origin/master') #//比较本地的master分支和origin/master分支的区别
    os.system('git merge origin/master')
    # os.system('git pull --rebase')
    # os.system('git pull')#//相当于进行了 git fetch 和 git merge两部操作
    os.system('git commit -m ' + '\"' + sys.argv[1] + '\"')#提交到本地仓库
    os.system('git push origin master') 

######不需要提交，提交的是public 目录下的文件




