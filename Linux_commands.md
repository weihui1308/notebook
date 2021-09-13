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

