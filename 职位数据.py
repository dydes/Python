import requests as re
import json
import pandas as pd
import time
import random

#获取网页url
def get_url(keyword,pn):
    base_url1 = "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput="    #不需要cookie的url
    base_url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"

    base_headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
                    "Host": "www.lagou.com",
                    "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
                    }
    data = {
            "first": "true",
            "pn": "{}".format(pn),
            "kd": "{}".format(keyword)
            }

    session = re.Session()      #创建cookie存储
    session.get(url=base_url1,headers=base_headers)        #通过网址url1建立cookie
    response = session.post(url=base_url, headers=base_headers, data=data)
    response.encoding = 'utf-8'
    #print(response)

    return response

#解析网页信息
def total_Count(response):

    page = response.json()
    # print(page)
    total_count = page['content']['positionResult']['totalCount']   #totalCount为总个数
    pn_count = int(total_count)//15 + 1
    #页数
    print('职位总数{},共{}页'.format(total_count,pn_count))
    return pn_count

def parse_url(response):
    page = response.json()
    for i in range(1,16):
        jobs_list = page['content']['positionResult']['result']
        #print(jobs_list)
        page_info_list = []             #用于存储data
        for i in jobs_list:
            job_info = []
            job_info.append(i['companyFullName'])
            job_info.append(i['companyShortName'])
            job_info.append(i['companySize'])
            job_info.append(i['financeStage'])
            job_info.append(i['district'])
            job_info.append(i['positionName'])
            job_info.append(i['workYear'])
            job_info.append(i['education'])
            job_info.append(i['salary'])
            job_info.append(i['positionAdvantage'])
            job_info.append(i['industryField'])
            page_info_list.append(job_info)
        print(page_info_list)
        return page_info_list

def save_data(page_info_list):
    df = pd.DataFrame(data=page_info_list,
                      columns=['公司全名', '公司简称', '公司规模', '融资阶段', '区域', '职位名称', '工作经验', '学历要求', '工资', '职位福利','行业'])
    #print(df)
    df.to_csv('lagou1_jobs.csv', index=False)
    print('保存完成')

#     #调用中心
def main():
    keyword = input('输入查找内容:')      #输入搜索内容
    a = get_url(keyword,pn=1)            #获取respones
    b = total_Count(a)                  # 获得数据总个数和页数
    total_info = []                     #用来储存每页parse_url
    for i in range(1,int(b)+1):         #实现翻页效果
        a = get_url(keyword, pn=i)
        c = parse_url(a)
        total_info += ci
        time.sleep(20)
        print('成功获取第{}页'.format(i))
    d = save_data(total_info)

if __name__ =="__main__":
    main()