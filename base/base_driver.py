from appium import webdriver


def init_driver(activity_name='.activities.PeopleActivity'):
    # 创建一个字典，包装相应的启动参数
    desired_caps = dict()
    # 需要连接的手机的平台(不限制大小写)
    desired_caps['platformName'] = 'android'
    # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
    desired_caps['platformVersion'] = '5.1'
    # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
    desired_caps['deviceName'] = 'huawei p30'
    # 需要启动的程序的包名
    desired_caps['appPackage'] = 'com.android.contacts'
    # 需要启动的程序的界面名
    desired_caps['appActivity'] = activity_name

    # 连接appium服务器
    return webdriver.Remote('http://192.168.31.50:4723/wd/hub', desired_caps)
