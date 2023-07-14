from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONE = {
    "日本": "Asia/Tokyo",
    "タイ": "Asia/Bangkok",
    "オーストラリア": "Australia/Sydney",
    "ロシア": "Europe/Moscow",
    "エジプト": "Africa/Cairo",
    "フランス": "Europe/Paris"
}


def get_time(request):
    # cors設定
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': 'https://main.d10gvnlkhilpg6.amplifyapp.com',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return ('', 204, headers)

    if request.method == 'GET':
        now = datetime.now(ZoneInfo(TIME_ZONE["日本"]))
        response = {'message': f'日本の現在時刻は{now}です'}
        headers = {'Access-Control-Allow-Origin': 'https://main.d10gvnlkhilpg6.amplifyapp.com'}
        return (response, 200, headers)


if __name__ == "__main__":
    get_time()
