# 基本功能运行

[https://github.com/seventyzlp/AirDrone](https://github.com/seventyzlp/AirDrone)

clone这个github仓库，将AirDroneClient.py设置成启动文件。并且在运行Unreal场景后执行这个python脚本。

![image.png](pic/image%201.png)

上面的两排按钮能够对无人机进行控制，但是指令的执行有延迟。最下面一排第一个下拉框在选中指定的天气后能够把当前飞机传送到那个天气的区域，并且也会触发那个天气动物的运动。

另外，传送是**非必须**的，可以直接控制无人机飞到那一块区域，同样能够触发动物运动。

如果想要使用**手柄控制**，那么需要在运行UE场景前把手柄连接好，并且在传送完之后点ExitApiControl这个按钮切换到手柄控制。

如果想要使用**键盘控制，**需要点击按钮EnableKeyboardControl，这会**强制占用所有键盘输入**，只有关掉这个程序才能中止。键盘wasd控制移动，方向键↑↓控制飞机升降，←→控制转向。

# 修改Api传送位置、飞行速度

让飞机在空中生成的原因是统一UE坐标与airsim坐标。在获取到UE传送目标坐标后，直接填到Api的传送函数里面即可。

上文中提及的Api控制APP的传送设置在DroneController这个文件里面。

![image.png](pic/image%202.png)

使用键盘控制的飞机飞行速度同样在这个文件中。

![image.png](pic/image%203.png)

数字越大速度越快，还能改按键绑定。
