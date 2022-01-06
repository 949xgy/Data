import time
import requests

import warnings

warnings.filterwarnings("ignore")


def request_data(url):
    global err_num
    result = None
    header = {
        'authority': 'api-cn.louisvuitton.cn',
        'method': 'GET',
        'path': '/api/zhs-cn/catalog/availability/007653',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'lv-dispatch=zhs-cn; lv-dispatch-url=https://www.louisvuitton.cn/zhs-cn/products/neverfull-mm-monogram-007653; OPTOUTMULTI=0:0%7Cc1:0%7Cc2:0%7Cc4:0%7Cc3:0; ak_cc=CN; _ga=GA1.2.2015977019.1641060111; Qs_lvt_187854=1641060111; Qs_pv_187854=238349738261507170; _gcl_au=1.1.1614606010.1641060112; _qubitTracker=586p73ra8u0-0kxw4til1-03ibfc4; qb_generic=:X4WzhdT:.louisvuitton.cn; _cs_c=1; _cs_id=86189283-9e6a-ac86-e224-96e9fcef93b0.1641060113.1.1641060113.1641060113.1.1675224113180; utag_main=v_id:017e16ce0a2300212abd65a7bfaa05098004809000978$_sn:1$_se:4$_ss:0$_st:1641061917818$ses_id:1641060108837%3Bexp-session$_pn:1%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session$dc_region:eu-central-1%3Bexp-session; qb_permanent=586p73ra8u0-0kxw4til1-03ibfc4:1:1:1:1:0::0:1:0:Bh0JcS:Bh0JcS:::::59.63.204.155:nanchang:14450:china:CN:28.44:116.01:nanchang:156124:jiangxi%20sheng:35604:migrated|1641060119785:FYks==B=CdwB=I0::X4WzjTp:X4Wzhy4:0:0:0::0:0:.louisvuitton.cn:0; ak_bmsc=9F3C9C7CCB6FC5AA0F4E8460BE00A541~000000000000000000000000000000~YAAQdOBb2nfQjbV9AQAAVNSaHg6nt9jsTANWhwVP0v6U2oW9qFj2/KdmnqwbEhFWK4biU/2XpaKBXMlV0Cv8ZDlk7uvuOM47aNGEHXSiRTI6dJ8c7Lul5VrlwU5Qkg5WgQKPVsheB7bN/nOJX9sGimTthpjcFGmhW3rKLSFMUsuZKsgY9py+AIpF4yNrPl3ZHggc8Q28IiI1twKCSAcAgeiU7nxR/pIsatVXDen/o0VByyTBB6mqmSf2SGcVBcmoiWoekrlNXBwGrBwHTkmyooubH9NK/CLqLGDn4sPXEiQWgU0T4yPbc1auVExehmCjDOmnKTPraQKD/j+7vEd4dddUoOB2gRjnrx2iYlTJWcXu6KebQCeE3yUTVWmu+WDtF6Fi1t4mhBf4sQ+EcAMFCg==; bm_sz=CB7DCE32FC1BB9B3569C8BCBEF6E0674~YAAQdOBb2njQjbV9AQAAVNSaHg4wtJhbau9wjQLkwLHogUVORbSIhryvnpxseXFZYjO3552htJtsATsSkwOkL/6IuocPq1v5UdJxkNtDKXm7ZCgVWdNjmYYcGPJ797Yu1eyRueBSfZV++0XMpnjvI6s0RlpMpvFREO4pspsouPzLpw0Gj/xAdxP52vg8oU/f3R4KkSB+YTrtXYTvxxGivZBwefHmJx6kL+BODGwfNpbuyq07NeGPqcq9FPVhsGL4vsEpXNg5jxQAoVudSngVWR+ipE0k+7PhBJWZa+pOu+IMfppVprXCoA==~3158083~3159857; _abck=94E255EFB082B9BBA126C5A3CB683753~0~YAAQdOBb2uPXjbV9AQAA9hOcHgeKAy4aAcuqyER1Q3vW3saSc8/y+gML7ihEvBJc/RC0Ut3wWWW3T9YAWkEr0ZSGL6C9vSeCqqPHtCNDF4m7NaYc20X6vPGNO0rDwr/Z8ykahjlZQXDUzdOuDllEKc/s7J+WQjG5pbqk8HSLeMJQWfiJ/UY+IDNgdyJd13rY0BkAMFfasKALF/7O06gKcoXjQNc3VwaT0YbGfakjo35RN/d//vNgljuzpVtLlzY8E239ilx8QwBJzyQsJDAhy3NOPoPnsdJz+uZO7SIn3BWqNW5ENWjDItCyVM63Ru9arbFbNytwtNF93yHeQZ4dHUrgKDxh2KChUi14bIlFDg18GokDKiLExkgAHDlWNvxo4S6LuvzBEQgyLewnr13ng+80d5dKYvxRAMC2/Fo=~-1~-1~1641063730',
        'upgrade-insecure-requests': '1',
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36',
    }
    try:

        result = requests.get(url=url, headers=header, verify=False)

    except:
        err_num = err_num + 1
        print('获取链接错误')

    return result


# 微信单人通知
def single_weixin_notification(msg, uids, url_shoop):
    token = "AT_h3GBjChS19kgeyQGAusiCPucHJEnCaAy"
    url = "http://wxpusher.zjiecode.com/api/send/message"
    body = {
        "appToken": token,
        "content": msg,
        "contentType": 3,
        "uids": [uids],
        "url": url_shoop  # 原文链接，可选参数
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url, headers=headers, json=body)
    print(response.text)


# 有货通知
def single_weixin_notification2(msg, url_shoop):
    token = "AT_h3GBjChS19kgeyQGAusiCPucHJEnCaAy"
    url = "http://wxpusher.zjiecode.com/api/send/message"
    body = {
        "appToken": token,
        "content": msg,
        "contentType": 3,
        "uids": ["UID_tDwWuoHjbfO93OOhah7y9B16qQRM",
                 "UID_apQSVILmPb7oiOqrdujGWhBfVnzj"
                 ],
        "url": url_shoop  # 原文链接，可选参数
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url, headers=headers, json=body)
    print(response.text)


def status(url):
    global no_num, yes_num, err_num
    name = ''  # 商品名字
    color = ''  # 商品颜色
    link = ''  # 商品链接 url[0]：商品链接,url[1]: 商品对应的api状态链接
    stock = ''  # 库存状态
    message = ''

    res = request_data(url[1])
    if res == None:
        return
    if res.status_code == 200:
        json_data = res.json()
        skuAvailability = json_data['skuAvailability']
        for i in range(len(skuAvailability)):
            skuId = skuAvailability[i]['skuId']  # 颜色编码
            inStock = skuAvailability[i]['inStock']  # 库存状态

            if skuId == 'M40995':
                name = 'NEVERFULL 中号手袋'
                color = 'Beige'
            elif skuId == 'M41177':
                name = 'NEVERFULL 中号手袋'
                color = 'Cherry'
            elif skuId == 'M41178':
                name = 'NEVERFULL 中号手袋'
                color = 'Pivoine'
            elif skuId == 'N41207':
                name = '配饰包'
                color = ''

            link = url[0] + '#' + skuId  # 对应商品链接

            if inStock:
                yes_num = yes_num + 1
                stock = '有货了！！'
                message = '''
>
>商品名称:**''' + name + '''**
>
>商品颜色:**''' + color + '''**
>
>库存状态:<span style="color:red;">''' + stock + '''</span>
>
>商品链接:[''' + link + '''](''' + link + ''')
>
>查询状态:已查询''' + str(no_num+yes_num) + '''遍！
---

'''

                if yes_num <= 2:
                    single_weixin_notification2(message, link)
                print(skuId, ':', inStock)
            else:
                no_num = no_num + 1
                if no_num % 2001 == 0:
                    stock = '没货'
                    message = '''
>
>商品名称:**''' + name + '''**
>
>商品颜色:**''' + color + '''**
>
>库存状态:<span style="color:red;">''' + stock + '''</span>
>
>商品链接:[''' + link + '''](''' + link + ''')
>
>查询状态:已查询''' + str(no_num) + '''遍！
---

'''

                    single_weixin_notification(message, "UID_tDwWuoHjbfO93OOhah7y9B16qQRM", link)
        print(skuAvailability)
    else:
        err_num = err_num + 1
        print('状态码错误！')
        return


if __name__ == '__main__':

    url = ["https://www.louisvuitton.cn/zhs-cn/products/neverfull-mm-monogram-007653",
           "https://api-cn.louisvuitton.cn/api/zhs-cn/catalog/availability/007653"]
    url2 = ["https://www.louisvuitton.cn/zhs-cn/products/pochette-accessoires-damier-azur-canvas-005868",
            "https://api-cn.louisvuitton.cn/api/zhs-cn/catalog/availability/005868"]
    err_num = 0
    yes_num = 0
    no_num = 0
    list_url = [url, url2]
    i = 0
    print('start')
    while 1:
        i = i % 2
        status(list_url[i])

        if err_num % 10 == 0 & err_num != 0:
            single_weixin_notification("错误了:" + str(err_num) + '次', 'UID_tDwWuoHjbfO93OOhah7y9B16qQRM', list_url[i][0])

        i = i + 1
        time.sleep(3)
