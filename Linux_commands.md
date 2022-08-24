## 文件传输
1. 一台机器上的复制  
    ````
    $ cp -i file1 file2
    将文档 file1复制成file2，复制后名称被改file2

    $ cp -i file1 dir1
    将文档 file1复制到dir1目录下，复制后名称仍未file1

    $ cp -r dir1 dir2
    将目录dir1下的所有文件复制到dir2目录下，复制结果目录被改名为dir2
2. 跨机器的文件传输
    ````
    $ scp local_file remote_username@remote_ip:remote_folder 
    $ scp /home/space/music/1.mp3 root@www.runoob.com:/home/root/others/music 
    从本地复制到远程

    $ scp root@www.runoob.com:/home/root/others/music /home/space/music/1.mp3 
    从远程复制到本地，调换顺序即可

    $ rsync -P --rsh=ssh local_file remote_username@remote_ip:remote_folder 
    传大文件时，失败了可以继续传
3. 传文件夹
    ````
    scp  -r /tmp/local_dir remote_username@remote_ip:remote_dir
    从本地上传到指定机器的文件夹下
## 文件解压缩
1. zip文件
    ````
    $ zip -r myfile.zip ./*
    将当前目录下的所有文件和文件夹全部压缩成myfile.zip文件,－r表示递归压缩子目录下所有文件.

    $ unzip -o -d /home/sunny myfile.zip
    把myfile.zip文件解压到 /home/sunny/
2. tar.gz文件
    ````
    $ tar -tzvf file.tar.gz
    查看tar包内包含的文件

    $ tar -zxvf file.tar.gz foder/access.log.0805
    解压单个文件

    $ tar -zxvf file.tar.gz foder/access.log.*
    解压多个文件

    $ tar -xzvf file.tar.gz foder/access.log.0805 -C /new/dir/    
    -C 指定解压到的目录.
## 查看
1. 查看磁盘的使用情况
    ````
    $ df -h
2. 查看文件大小
    ````
    $ ls  -l    filename
3. 查看当前文件夹占磁盘空间大小
    ````
    $ du    -sh
4. 查看当前目录下的文件数量（不包含子目录中的文件）
    ````
    $ ls -l|grep "^-"| wc -l
5. 查看当前目录下的文件数量（包含子目录中的文件） 注意：R，代表子目录
    ````
    $ ls -lR|grep "^-"| wc -l
6. 查看当前目录下的文件夹目录个数（不包含子目录中的目录），同上述理，如果需要查看子目录的，加上R
    ````
    $ ls -l|grep "^d"| wc -l
7. 查看当前目录下.jpg文件的数量
    ````
    $ ls -lR | grep "jpg" | wc -l
8. ncdu命令
    ````
    $ sudo apt install ncdu
    Ubuntu下安装
    $ ncdu
    扫描当前目录，并且按照文件及文件夹占用大小，从大到小排列
    $ d
    删除文件
    $ q
    退出
    $ ?
    快捷键提示
    $ ncdu 目录
    扫描指定目录的信息
## 复制、移动和删除
1. 文件夹
    ````
    $ cp -r dir1 dir2
    dir2目录不存在，可以直接使用

    $ rm -rf dir

    $ mv info/ logs  
    将 info 目录放入 logs 目录中。注意，如果 logs 目录不存在，则该命令将 info 改名为 logs。
2. 文件
    ````
    $ cp -i filename dir1
    $ rm -f filename
    $ mv aaa bbb
## tmux的使用
1. 查看会话
    ````
    $ tmux ls
    # or
    $ tmux list-session
    ````
2. 接入会话
    ````
    # 使用会话编号
    $ tmux attach -t 0

    # 使用会话名称
    $ tmux attach -t <session-name>
    ````
3. 杀死会话
    ````
    # 使用会话编号
    $ tmux kill-session -t 0

    # 使用会话名称
    $ tmux kill-session -t <session-name>
    ````
4. 新建会话
    ````
    tmux new -s <session-name>
    ````
## conda相关命令
1. 创建环境
    ````
    conda create -n your_env_name python=X.X
2. 删除环境
    ````
    conda remove -n your_env_name --all
3. 查看环境
    ````
    conda info --env