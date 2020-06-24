1. shell编写使用规范

   + 指定当前脚本要使用的shell解释器

   ```bash
   #!/bin/bash                           
   ```

   * 文件名要以`.sh` 为结尾
     * `filename.sh`
   * 使用时要确保脚本有执行权限，并且以`./filename.sh`的形式执行或者 `bash filename.sh`
     * 只输入`filename.sh`的话，Linux会在PATH里寻找文件而不是当前路径中寻找
   * 建议使用双引号

2. 变量

   + 使用`var=value`的形式来创建变量，等号两边不能有空白

   + 变量名只能使用数字，字母，下划线，且不能以数字开头

   + 使用变量时，需要加`$`

     ```bash
     #!/bin/bash
     content="hello world"
     echo $content
     ```

   + 变量的值为一个命令的返回值时，通常命令后会带空格，所以命令整体要用反引号`包围

     ```bash
     #!/bin/bash
     date_time=`date +"%F %T"`
     echo $date_time
     ```

   + `readonly ` var，设置var为只读变量

     + 只读变量只可读，不可修改

     ```bash
     #!/bin/bash
     var=1
     readonly var
     echo $var
     #var=2 will cause a error
     ```

   + `read -p` message var，提示message接收用户输入，保存为var

     + 读取用户想创建的目录名，自动创建目录

     ```bash
     #!/bin/bash
     read -p "Enter the directory name you want to create:" dir_name
     mkdir $dir_name
     ```

   + `unset` var，删除变量var
