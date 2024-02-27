# easy_lottery_tools



### 控制台版本用法如下：

1. 此抽奖程序只需要配置result.csv
格式就是一行，一个人名+序号+编号
![image](https://github.com/sklfihggczx/easy_lottery_tools/assets/158799119/405811c7-f1b7-4414-b883-3e7f5e28013e)

3. 在控制台（请不要用ide运行）输入：

    ```sh
    python main_cli.py
    ```

4. 首先程序会自动读取并打印成绩信息，成绩为权重，然后等待键盘输入

命令介绍：

- `info`：输出当前成员信息；
- `del user_id`：手动删除成员；
- `roll prize num`：开始抽奖，抽`num`次，默认以0.05秒的时间间隔滚动，滚动期间按下Ctrl+C停止滚动，抽下一位。每抽出一个用户会自动从抽奖列表中剔除该用户；
- `pub`：打印获奖信息。

### 图形化版本用法如下：
1. 此抽奖程序只需要配置result.csv
格式就是一行，一个人名+序号+编号
![image](https://github.com/sklfihggczx/easy_lottery_tools/assets/158799119/c0601a5f-dc6e-46d0-9be5-2a83ad6cc3cf)

2.使用 Python 3.10 及以上版本并安装 PyQt6 库，双击 `main_gui.pyw` 即可。

![image](https://github.com/sklfihggczx/easy_lottery_tools/assets/158799119/887123f3-15c3-4e00-bbdb-e7f4e236d881)

