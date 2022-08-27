from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request
from selenium.webdriver.common.by import By

class cupangimage():
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)



    keyword='눈에 좋은 차'
    createFolder('./images') ##blink 이미지랑 같은 느낌

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--headless') # 창 없는 모드
    # headless 모드의 호환성을 위해 아래 옵션 추가(가끔 막는 웹이 있음)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    chrome_options.add_argument("lang=ko_KR") # 한국어
    chrome_options.add_argument('window-size=1920x1080')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('chromedriver',options=chrome_options)
    driver.implicitly_wait(3)


    # =============================================================================
    # 쿠팡 이미지 검색 접속 및 검색어 입력
    # =============================================================================
    print(keyword, '검색')
    driver.get('https://www.coupang.com/np/search?q='+keyword+'&channel')


    # Keyword=driver.findElement(By.xpath('//*[@id="sbtc"]/div/div[2]/input'))
    # #Keyword = driver.find_element_by_xpath(r'//*[@id="sbtc"]/div/div[2]/input')
    # Keyword.send_keys(keyword)
    # driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

    # Keyword=driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    # Keyword.send_keys(keyword)



    # =============================================================================
    # 스크롤
    # =============================================================================
    # print(keyword+' 스크롤 중 .............')
    # elem =  driver.find_element(By.TAG_NAME,("body"))
    # for i in range(60):
    #     elem.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.1)
        

    # =============================================================================
    # 이미지 개수
    # =============================================================================
    links=[]
    images = driver.find_elements(By.CSS_SELECTOR,("img.search-product-wrap-img"))
    cnt=0
    for image in images:
        if image.get_attribute('src')!=None:
            links.append(image.get_attribute('src'))
            cnt+=1
        if cnt==3:
            break
        
    print(keyword+' 찾은 이미지 개수:',len(links))
    time.sleep(2)


    # =============================================================================
    # 이미지 다운로드
    # =============================================================================
    cnt=0
    for k,i in enumerate(links):
        url = i
        start = time.time()
        urllib.request.urlretrieve(url, "./images/"+keyword+"_"+str(k)+".png")
        print(str(k+1)+'/'+str(len(links))+' '+keyword+' 다운로드 중....... Download time : '+str(time.time() - start)[:5]+' 초')
        cnt+=1
        if cnt==3:
            break
    print(keyword+' ---다운로드 완료---')

    driver.close()
