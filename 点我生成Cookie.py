from DrissionPage import ChromiumPage
import json

page = ChromiumPage()

url = 'https://tieba.baidu.com/'

# 保存cookie
def get_cookie():
    page.get(url)
    input('请完成登录后按回车继续...')
    cookies_list = page.cookies(all_info=True)
    print('共拿到 {} 条 cookie'.format(len(cookies_list)))
    # 保存到本地
    with open('tieba_cookies.json', 'w', encoding='utf-8') as f:
        json.dump(cookies_list, f, ensure_ascii=False, indent=2)
    print('已写入 tieba_cookies.json')

if __name__ == '__main__':
    get_cookie()