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

3. 条件判断：`if` `elif ` `else` `then` `fi`

   + 关键字有两个其他语言不多见的`then`和`fi`，要注意，其中`fi`为`if`的闭合

     ```bash
     #!/bin/bash
     if condition
     then
     		command
     elif condition
     		command
     else
     		command
     fi
     ```

   + 单行判断可以用`;`来分割语句（一般在命令行中执行时使用）

     ```shell
     if [ condition ]; then command; fi
     ```

4. 运算符

   + 表达式计算工具

     + `expr`，可以完成表达式的求值操作

     ```bash
     #!/bin/bash
     read -p "请输入第一个数字: " var1
     read -p "请输入第二个数字: " var2
     res=`expr $var1 + $var2` #表达式，运算符前后必须有空格，完整的表达式要用反引号``包围
     echo "两数之和为: " $res
     ```

   + 算术运算符（既支持数字也支持字符串）

     + `+` 加法
       + `expr $a + $b`
     + `-` 减法
       + `expr $a - $b`
     + `*` 乘法
       + `expr $a \* $b`，需要转义
     + `/` 除法（整除）
       + `expr $a / $b`
     + `%` 取余
       + `expr $a % $b`
     + `=` 赋值
       + `a=$b`
     + `==` 判断相等（条件表达式要放在中括号`[]`里，并且括号前后和运算符前后要有空格）
       + `[ $a == $b ]`
     + `!=`  判断不相等
       + `[ $a != $b ]`

     ```bash
     #!/bin/bash
     a=7
     b=2
     
     echo "a = " $a
     echo "b = " $b
     
     echo "a + b" `expr $a + $b`
     echo "a - b" `expr $a - $b`
     echo "a * b" `expr $a \* $b`
     echo "a / b" `expr $a / $b`
     echo "a % b" `expr $a % $b`
     
     c=$a
     echo "c = " $c
     
     if [ $a == $c ]
     then
     		echo "a == c"
     fi
     
     if [ $a != $b ]
     then
     		echo "a != b"
     else
     		echo "a == b"
     fi
     ```

   + 关系运算符（运算对象为数字，或者值为数字的字符串，返回true/false）

     + `-eq`，equal，=
       + `[ $a -eq $b ]`
     + `-ne`，not equal，!=
       + `[ $a -ne $b ]`
     + `-gt`，great than，>
       + ` [ $a -gt $b ]`
     + `-lt`，less than，<
       + `[ $a -lt $b]`
     + `-ge`，great than or equal，>=
       + `[ $a -ge $b ]`
     + `-le`，less than or equal，<=
       + `[ $a -le $b ]`

   + 逻辑运算符（运算对象为条件，返回true/false）

     + `!`，非
       + `[ ! condition1 ]`
     + `-o`，或
       + `[ condition1 -o condition2 ]`
     + `-a`，与
       + `[ condition1 -a condition2 ]`

   + 字符串运算符（运算对象为字符串）

     + `=` ，判断字符串是否相等
       + `[ $a = $b ]`
     + `!=`，判断字符串是否不相等
       + `[$a != $b ]`
     + `-z`，`-n`，判断字符串长度是否为0
       + `[ -z $a ]`
       + `[-n $a ]`
     + 字符串也可直接作为条件，判断是否为空
       + `[ $a ]`

   + 文件测试运算符

     + `-d`，检测是否为目录
       + `[ -d $path ]`
     + `-f`，检测是否为文件
       + `[ -f $path ]`
     + `-r`，检测是否可读
       + `[ -r $path ]`
     + `-w`，检测是否可写
       + `[ -w $path ]`
     + `-x`，检测是否可执行
       + `[ -x $path ]`
     + `-e`，检测是否存在
       + `[ -e $path ]`
     + `-s`，检测是否非空
       + `[-s $path ]`

5. shell脚本传递接收参数

   + 在脚本中可以用`$`加上参数对应的index来表示，如`$1`代表第一个参数，`$0`代表脚本名自身

   ```bash
   #!bin/bash
   echo "$1 + $2 = "`expr $1 + $2`
   ```

   
