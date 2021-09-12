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
