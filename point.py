#從富邦網站抓分點資訊（看會不會比較好抓）
import requests
#https://fubon-ebrokerdj.fbs.com.tw/z/zg/zgb/zgb0.djhtm?a=6010&b=6010&c=B&e=2020-2-16&f=2020-2-17
#https://fubon-ebrokerdj.fbs.com.tw/z/zg/zgb/zgb0.djhtm?a=9800&b=9800&c=B&e=2020-2-17&f=2020-2-17
url = 'https://fubon-ebrokerdj.fbs.com.tw/z/zg/zgb/zgb0.djhtm?a=6010&b=6010&c=B&e=2020-2-16&f=2020-2-17'
#a:大分點；b:次分點；c:統計方式（B：金額；E：張）；d:區間；e:開始日期；f=結束日期
url = 'https://fubon-ebrokerdj.fbs.com.tw/z/zg/zgb/zgb0.djhtm?a={}&b={}&c={}&e={}&f={}'

#先取得券商代碼：select name="sel_Broker"
#再分別取得分公司代碼：select name="sel_BrokerBranch"
