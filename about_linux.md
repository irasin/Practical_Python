1. `vim`，能用`vim`就别用`vi`了吧

   1. 光标移动
      + h，j，k，l分别是left，down，up，right
      + 跳转到x行： xgg
      + 下一个单词：w，上一个单词：b
      + 下一页：ctrl + f，上一页：ctrl + b
      + 下x行：xj，上x行：xk
   2. 编辑
      + 插入：i，替换：r，追加：a
      + 复制：yy，剪切：cc，yxy或者cxc代表复制或剪切x行
      + 撤销：u，粘贴：p
      + 删除一个字符：x，删除整行：dd，删除到行尾：d$
      + 查找：/或者？，下一个：n，上一个；shift + n
      + 自动补全：ctrl + n
   3. 命令模式
      + :q 退出
      + :w 保存，可加文件名
      + :q! 强制退出
   4. .vimrc配置，建议去github上下载个别人的
      + :syntax on，语法高亮
      + :set number，显示行号

2. 字符通配符

   + `*` 匹配任意个数字符
   + `?` 匹配任意一个字符
   + `[]` 匹配括号中任意一个字符
     + `[abc]` 匹配abc中任意一个
     + `[a-f]` 匹配a到f中任意一个

3. `ls`  dir

   + `-a` 显示所有文件

   - `-l` 显示详细信息
   - `-h` 配合 -l使用，显示易于阅读的文件大小

4. `cd `  dir

   + `cd ~`或直接输入`cd`直接回到用户家目录
   + `cd -`切换到上一个使用的目录

5. `mkdir ` dir

   + `-p` 递归创建目录

6. `rm` dir/file

   +  `-r` 递归删除目录
   +  `-f` 强制删除

7. `tree` dir

   + `-d` 只显示目录，不显示文件

8. `cp` dir/file

   + `-i`  覆盖文件前提示
   + `-r` 递归复制src目录，dst也必须为目录

9. `mv` dir/file

   + `-i` 覆盖文件前提示

10. `cat` file

    + `-b` 对非空输出行编号
    + `-n` 对所有输出行编号

11. `more` /`less`  file (less更有用)

12. `grep` string  file

    + `-n`  显示行号
    + `-v`  显示不匹配行
    + `-i `  忽略大小写
    + 常用的两种查找模式
      + `^a` 搜索行开头为a的
      + `a$` 搜索行结尾为a的

13. `echo` string

    + 通常与重定向符号`>`，`>>` 配合使用

14. 重定向： 将本来显示在终端的内容 **输出**/**追加**到指定文件中

    + `>`  输出（会覆盖原文件）
    + `>>` 追加（会将内容追加到原文件的末尾）

15. 管道`|`：将**一个命令的输出**作为**另一个命令的输入**

    + 常用的管道命令 `more` ， `grep`
      + `ls -alh | less`  将`ls`的结果用`less`查看
      + `ls -alh | grep vi ` 对`ls`的结果通过`grep`查看含有vi的内容

16. `shutdown` 默认一分钟后重启

    + `-r` 重启

17. `ifconfig` 查看和设置网卡配置

18. `ping`  ip_address  

19. `ssh`  user@remote

    + `-p` port，默认22

20. `scp` src_path  user@remote`:`dst_path    

    +  `-P` port与`ssh` 不同，指定端口号时需要大写
    +  `-r`  递归复制目录
    +  服务器端的文件需要加冒号`:`

21. `ssh` `scp `免密码设置

    + `ssh-keygen` 配置公钥 
    + `ssh-copy-id` [-p port] user@remote 上传至服务器

22. `ssh` `scp `配置别名

    + 创建`~/.ssh/config`

    + 添加以下内容，{ }中的内容对应修改

      ```shell
      Host {server_name}
      		HostName {ip_address}
      		User {user_name}
      		Port {port_number}
      		
      #example:
      #Host tigersX
      #		HostName {192.168.100.1}
      #		User irasin
      #		Port 22
      #
      #设置完之后，
      #ssh tigers即可登录服务器
      #scp 1.py  tigers:1.py即可复制文件
      ```

23. `chomod` 777 dir/file，修改权限

    + `-R` ，递归修改

    + 权限对应的数字，read: 4，write: 2，excuse: 1
    + 三个数字对应user, group, others，777代表所有人可读可写可执行

24. `chown` user_name dir/file ，修改dir/file的所有者

    + `-R`，递归修改

25. `su`  user_name，是substitute user的缩写，表示使用另一个用户的身份，默认使用root用户

    + `exit` 退出当前登陆用户

26. `sudo` 以root权限执行

27. 关于group的操作，需要`sudo`权限

    + `groupadd` group_name，添加group
    + `groupdel` group_name，删除group
    + `cat /etc/group`，确认group信息
    + `chgrp` group_name dir/file，修改dir/file所属的组
      + `-R` 递归修改

28. 关于user的操作，需要`sudo`权限

    + `useradd` user_name，创建用户
      + `-m`，创建用户home目录
      + `-g` group_name，指定所属group
      + 也可以直接用`adduser`创建，创建时自动添加用户home目录，并需要输入密码
    + `passed` user_name，设置密码
    + `userdel` user_name，删除目录
      + `-r`，删除用户home目录
    + `cat /etc/passwd`，确认所有用户
    + 查看user信息
      + `id ` user_name，查看user的UID与GID
      + `who`，查看当前所有登录的用户列表
      + `whoami`，查看当前登陆用户名
    + 设置user的主组（GID）与附加组，以及登陆shell
      + `usermod -g` group_name user_name，修改user的主组（GID）
      + `usermod -G` group_name user_name，修改user的附加组（一般用于追加权限）
        + `usermod -G sudo irasin`，将irasin添加到sudo组
      + `usermod -s /bin/bash` user_name，修改user登陆的shell为bash
        + ubuntu中默认的shell为`dash`，然而这个不好用，建议修改
    + `which` cmd 查看命令所在路径

29. 系统信息相关命令

    1. 时间和日期
       + `date`，查看时间
       + `cal`，查看日历（calendar）
         + `-y` ，查看一年日历
    2. 磁盘与目录空间
       + `df`，显示剩余磁盘大小（disk free）
         + `-h`，方便人类阅读
       + `du` dir，显示目录下的文件大小（disk usage）
         + `-h`，方便人类阅读
    3. 进程信息
       + `ps`，查看进程的状态（process status），默认显示当前用户启动的进程
         + `ps aux` ，使用`ps`命令时不需要`-`
           + `a`，显示所有进程，包括其他用户的
           + `u`，显示进程详细信息
           + `x`，显示没有控制终端的进程
       + `top`，动态显示运行中的进程并且排序
         + 退出时使用`q`
       + `kill` PID，关闭进程
         + `-9`，强制关闭

30. `find` [path] -name "*py"，在path下搜索名字结尾为py的文件/目录，path默认为当前目录

    + 一般与通配符一起使用

31. ln -s src dst，建立src的软链接，保存到路径dst

    + `-s`表示创建软链接，没有的话表示硬链接（一般不使用硬链接）
      + 硬链接的源文件删除后，硬链接的文件也不受影响
        + 理由：linux中，文件名和文件数据时分开存储的，硬链接相当于创建一个源文件的文件数据的另外一个文件名，所以删除源文件也不会受影响

    + 源文件src要使用绝对路径
      + 不然移动软链接后，指向失效

32. 归档/压缩

    1. `tar` ，归档/解档

       + `tar -cvf ` dst.tar  src1 src2，将src1和src2归档为dst.tar
         + `-c`，归档
         + `-v`，显示过程
         + `-f`，指定档案文件名，所以放最后
       + `tar -xvf` dst.tar，解档dst.tar
         + `-x` ，解档
       + `-k`

    2. `gzip`，压缩/解压缩

       + `gzip` file，压缩文件
       + `gzip -d` file，解压缩文件

    3. `tar`与`gzip`可以同时使用，只需在`tar`里添加参数`-z`

       + `tar -zcvf` dst.tar.gz src1 src2
       + `tar -zxvf` dst.tar.gz 
         + `-C`解压缩到目标目录

    4. `bzip2`，压缩/解压缩，和`gzip`一样，在`tar`里添加参数`-j`可同时归档压缩

       + `tar -jcvf` dst.tar.bz2 src1 src2

       + `tar -jxvf` dst.tar.bz2
         + `-C ` path，解压缩到目标路径

33. `apt`，Advanced Packaging Tool，Linux下的安装包管理工具

    + 常用的命令
      + apt install 
      + apt remove
      + apt upgrade

    |     apt 命令     |      取代的命令      |           命令的功能           |
    | :--------------: | :------------------: | :----------------------------: |
    |   apt install    |   apt-get install    |           安装软件包           |
    |    apt remove    |    apt-get remove    |           移除软件包           |
    |    apt purge     |    apt-get purge     |      移除软件包及配置文件      |
    |    apt update    |    apt-get update    |         刷新存储库索引         |
    |   apt upgrade    |   apt-get upgrade    |     升级所有可升级的软件包     |
    |  apt autoremove  |  apt-get autoremove  |       自动删除不需要的包       |
    | apt full-upgrade | apt-get dist-upgrade | 在升级软件包时自动处理依赖关系 |
    |    apt search    |   apt-cache search   |          搜索应用程序          |
    |     apt show     |    apt-cache show    |            显示细节            |



|   新的apt命令    |              命令的功能              |
| :--------------: | :----------------------------------: |
|     apt list     | 列出包含条件的包（已安装，可升级等） |
| apt edit-sources |              编辑源列表              |

33. 配置软件源/镜像源
    + 国内可以用阿里云，清华，搜狐等镜像源
34. `wget`与`curl`，都支持下载文件，略有差别(https://blog.csdn.net/weixin520520/article/details/106828648?ops_request_misc=&request_id=&biz_id=102&utm_term=ubuntuwget curl&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-106828648)
    + `wget ` [-O name] url，下载并保存为name，也可以不加参数直接保存
    + `curl -o name` url，下载并保存为name，必须加参数

35. 安装anancoda
    + `wget` https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
    + `bash` Anaconda3-2020.02-Linux-x86_64.sh
