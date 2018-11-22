import requests,time,os
from selenium import webdriver
def shse(name):#√
    driver = webdriver.Edge()
    driver.maximize_window()  # 最大化浏览器，方便截图
    driver.get('http://www.sse.com.cn/disclosure/credibility/supervision/measures/')
    time.sleep(5)
    # 网页操作：输入、点击查询
    buttonElem = driver.find_element_by_id('btnQuery')
    nameElem = driver.find_element_by_id('inputCode')
    nameElem.clear()
    nameElem.send_keys(name)
    buttonElem.click()
    time.sleep(20)
    # ★判断是否有处罚。没有处罚的，pdfElem会返回空列表；找了几个处罚案例，基本上pdf链接的名称会带上"的决定"
    pdfElem = driver.find_elements_by_partial_link_text('的决定')
    if pdfElem == []:
        driver.save_screenshot(".\\上交所_查询结果\\%s.png" % (name + '_无处罚文件'))
        print(name + '：上交所无处罚文件，已截图')
    else:
        driver.save_screenshot(".\\上交所_查询结果\\%s.png" % (name + '_处罚汇总'))
        print(name + '上交所有处罚文件，已截图，待下载pdf')
        # 网页中大约每个显示出来的链接，后面还有4个显示不出来的；需要筛选是否重复
        linkList=[]
        a=1
        for i in range(len(pdfElem)):
            url = pdfElem[i].get_attribute('href')
            if url not in linkList:
                linkList.append(url)
                res = requests.get(url)
                res.raise_for_status()
                time.sleep(10)
                open('.\\上交所_查询结果\\%s_处罚纪录_%d.pdf' % (name, a), 'wb').write(res.content)
                print(name + '上交所处罚纪录已保存' + str(a) + '份')
                a+=1
        print(name + ' 上交所处罚纪录保存完毕，合计' + str(a - 1) + '份')
    driver.quit()

print('请输入需要查询的证券代码，以空格间隔。如：601798 600712 601595')
nameSH = input()
st = time.time()
SHlist = nameSH.split(' ')
path='.\\上交所_查询结果'
if not os.path.exists(path):
    os.mkdir(path)
for name in SHlist:
    shse(name)




