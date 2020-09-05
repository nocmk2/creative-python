# 实验环境
让我们来一步一步搭建一个python并发编程的实验环境

## Nginx
### 下载Nginx https://nginx.org/en/download.html
mac下可以通过brew安装Nginx：
``` shell
brew search nginx
brew install nginx
```
如果你使用windows可以参考官方这篇
https://nginx.org/en/docs/windows.html

启动nginx
```
nginx
```

查看nginx的配置
``` shell
nginx -V
```
--conf-path后面的是配置文件,打开配置文件增加server配置
```
    server {
        listen       8021;

        location / {
            root   你的工作目录/creative-python/data/flags/;
        }
    }
```

解压creative-python/data/flags.zip

重新加载nginx新的配置
``` shell
nginx -s reload
```

打开
http://localhost:8021/cn/cn.gif
如果看到国旗说明服务启动成功


## Vaurien

## Toxiproxy





## 参考资料
https://github.com/fluentpython/example-code/tree/master/17-futures-py3.7/countries