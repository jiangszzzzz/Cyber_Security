## 2 Command Injection
命令注入。输入 127.0.0.1 点submit。等四秒出现以下。

![](img/img_8.png)

同样 brupsuit intercept on。 输入127.0.0.1 后，查看报文。 ctrl + r 。

修改报文，可以执行 whoami dir 等命令。 ctrl + u 转换url编码。

![img.png](img/img_9.png)

    echo test > test.php 

上传一句话木马。

echo “111” > 1.php 会写入“”， 采用 ^<php  ^> 方式写入，如下图。

![img.png](img/img11.png)

![img.png](img/img10.png)

使用antsword连接。

github 下载antsword。

![img.png](img/img12.png)

如果执行命令行 会被defend杀。

![img.png](img/img13.png)