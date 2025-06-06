import requests
from barkSend import SendBark

key = "aedc97eaa1fd4b148476a0afa47c60ee"  # key


def get_location_id(loc):
    # 中国城市代码查询
    location_url = f"https://geoapi.qweather.com/v2/city/lookup?location={loc}&key={key}"

    location_resp = requests.get(location_url)
    location_id = location_resp.json()['location'][0]['id']
    return location_id

def get_weather(loc_id):
    # 实时天气查询
    weather_url = f"https://devapi.qweather.com/v7/weather/now?location={loc_id}&key={key}"
    weather_resp = requests.get(weather_url)
    # print(weather_resp.json())
    # obs_time = weather_resp.json()['now']['obsTime'] # 观测时间

    update_time = weather_resp.json()['updateTime'] # 更新时间
    temp = weather_resp.json()['now']['temp']  # 温度
    feels_like = weather_resp.json()['now']['feelsLike']  # 体感温度
    text = weather_resp.json()['now']['text']  # 天气
    wind_dir = weather_resp.json()['now']['windDir']  # 风向
    wind_scale = weather_resp.json()['now']['windScale']  # 风力等级

    # wind360 = weather_resp.json()['now']['wind360'] # 风向360角度
    # wind_speed = weather_resp.json()['now']['windSpeed'] # 风速
    # humidity = weather_resp.json()['now']['humidity'] # 湿度
    # precip = weather_resp.json()['now']['precip'] # 降水量
    # pressure = weather_resp.json()['now']['pressure'] # 大气压强
    # vis = weather_resp.json()['now']['vis'] # 能见度
    # cloud = weather_resp.json()['now']['cloud'] # 云量
    # dew = weather_resp.json()['now']['dew'] # 露点温度
    return update_time,text,temp,feels_like,wind_dir,wind_scale

pd_loc_id = get_location_id("pudong")
pz_loc_id = get_location_id("pizhou")
pd_weather = get_weather(pd_loc_id)
pz_weather = get_weather(pz_loc_id)

show_time = pd_weather[0].split("+")[0].replace("T", " ")
content = f"""
✅浦东: {pd_weather[1]}，{pd_weather[2]}°C，体感: {pd_weather[3]}°C，{pd_weather[4]}{pd_weather[5]}级

✅邳州: {pz_weather[1]}，{pz_weather[2]}°C，体感: {pz_weather[3]}°C，{pz_weather[4]}{pz_weather[5]}级

❤️信息来源：和风天气
"""

# 发送到bark
bark_key = "UZ9juRSNtAMpnzWEQokJYF"
bark = SendBark(bark_key)
bark.send_t_c(show_time,content)
