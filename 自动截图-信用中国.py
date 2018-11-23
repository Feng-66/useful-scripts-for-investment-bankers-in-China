import requests,time,os
from selenium import webdriver
def creditCH(fullname):#静态网页但是抓不到
    param={"index":0,"keyword":fullname}
    res = requests.get('https://www.creditchina.gov.cn/xinyongxinxi/index.html', params=param)
    res.encoding='UTF-8'#网站所用的编码，防止request搞错
    driver = webdriver.Edge()
    driver.maximize_window()  # 最大化浏览器，方便截图
    driver.get(res.url)
    time.sleep(5)
    coLinks=driver.find_elements_by_class_name('company-item  class=')
    nextLinks = driver.find_elements_by_class_name('page-link next')
    while not nextLinks==[]:
        for i in range(len(coLinks)):  # 每个按钮点一遍，从而打开每个搜索结果；每个搜索结果中点‘下载信用报告’调至详情页
            coLinks[i].click()
            time.sleep(2)
        nextLinks[0].click()
        time.sleep(5)#需要暂停等网页加载，加载未完成会出现Error：Stale element reference
        coLinks = driver.find_elements_by_class_name('company-item  class=')
        nextLinks = driver.find_elements_by_class_name('page-link next')
    now_handle = driver.current_window_handle
    all_handles = driver.window_handles
    a = 1
    for handle in all_handles:
        if handle != now_handle:
            driver.switch_to.window(handle)
            button = driver.find_element_by_class_name('add-ons-btn1')
            button.click()
            time.sleep(5)
            # ★★★★★滚动界面至底部以截图；OR 选择点击下载按钮，但需设置浏览器的属性确保不弹窗和路径
            height = driver.execute_script("return document.body.clientHeight")
            k = 1
            while True:
                if k * 500 < height:
                    driver.save_screenshot(".\\信用中国_查询结果\\%s_%d(%d).png" % (fullname, a, k))
                    # Edge无法截长图...
                    js_move = "window.scrollTo(0,{})".format(k * 500)
                    driver.execute_script(js_move)
                    time.sleep(2)
                    height = driver.execute_script("return document.body.clientHeight")
                    k += 1
                else:
                    break
            a += 1
    print(fullname + ' 信用中国截图保存完毕，合计' + str(a - 1) + '份')
    driver.quit()

print('请输入需要查询的公司全称，以空格间隔。如：中国通用 小米科技有限责任公司')
fullnameAll=input()
st = time.time()
fullnamelist=fullnameAll.split(' ')
path='.\\信用中国_查询结果'
if not os.path.exists(path):
    os.mkdir(path)
for name in fullnamelist:
    creditCH(name)



