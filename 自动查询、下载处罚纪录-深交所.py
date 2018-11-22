import requests,time,os
from selenium import webdriver
def szse(name):#√
    driver = webdriver.Edge()
    driver.maximize_window()  # 最大化浏览器，方便截图
    driver.get('http://www.szse.cn/disclosure/listed/credit/record/index.html')
    time.sleep(5)
    nameElem=driver.find_element_by_id('1759_cxda_tab1_txtDsr')
    buttonElem=driver.find_element_by_class_name('confirm-query btn-query-primary')
    nameElem.clear()
    nameElem.send_keys(name)
    buttonElem.click()
    time.sleep(20)
    pdfElem = driver.find_elements_by_link_text('查看')#判断是否有处罚。没有处罚的，pdfElem会返回空列表
    if pdfElem==[]:
        driver.save_screenshot(".\\深交所_查询结果\\%s.png" % (name + '_无处罚'))
        print(name + '：深交所无处罚纪录，已截图')
    else:
        driver.save_screenshot(".\\深交所_查询结果\\%s.png" % (name + '_处罚汇总'))
        print(name + '深交所有处罚，已截图，待下载pdf')
        a=1
        for i in range(len(pdfElem)):
            partial_url=pdfElem[i].get_attribute('encode-open')
            url='http://reportdocs.static.szse.cn/'+partial_url
            res=requests.get(url)
            res.raise_for_status()
            time.sleep(10)
            open('.\\深交所_查询结果\\%s_处罚纪录_%d.pdf'%(name,a),'wb').write(res.content)
            print(name+'深交所处罚纪录已保存'+str(a)+'份')
            a = a + 1
        print(name+' 深交所处罚纪录保存完毕，合计'+str(a-1)+'份')
    driver.quit()

print('请输入需要查询的证券简称，以空格间隔。如：丹邦科技 荣之联 尔康制药')
nameSZ = input()
st = time.time()
SZlist = nameSZ.split(' ')
path='.\\深交所_查询结果'
if not os.path.exists(path):
    os.mkdir(path)
for name in SZlist:
    szse(name)





