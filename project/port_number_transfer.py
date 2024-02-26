import requests


def get_port_number(mobile):
    response = requests.get(f"http://xhapi.idcdun.com/api.php?mobile={mobile}")
    return response.json()


res = get_port_number(input("请输入手机号码：\n\n"))


if res["code"] == 0:
    is_transfer = res["result"]["res"] == 1
    print(
        f"当前手机号：{res['result']['Mobile']}， {'已' if is_transfer else '未'}转网"
    )
else:
    print(res["reason"])
