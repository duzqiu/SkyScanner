import requests
from barkSend import SendBark

key = "aedc97eaa1fd4b148476a0afa47c60ee" # key

# 中国城市代码查询
location = "pudong" # 地点
location_url = f"https://geoapi.qweather.com/v2/city/lookup?location={location}&key={key}"

location_resp = requests.get(location_url)
location_id = location_resp.json()['location'][0]['id']
# print(location_id)

# 实时天气查询
weather_url = f"https://devapi.qweather.com/v7/weather/now?location={location_id}&key={key}"
weather_resp = requests.get(weather_url)
# print(weather_resp.json())
update_time = weather_resp.json()['updateTime'] # 更新时间
obs_time = weather_resp.json()['now']['obsTime'] # 观测时间
temp = weather_resp.json()['now']['temp'] # 温度
feels_like = weather_resp.json()['now']['feelsLike'] # 体感温度
text = weather_resp.json()['now']['text'] # 天气
wind360 = weather_resp.json()['now']['wind360'] # 风向360角度
wind_dir = weather_resp.json()['now']['windDir'] # 风向
wind_scale = weather_resp.json()['now']['windScale'] # 风力等级
wind_speed = weather_resp.json()['now']['windSpeed'] # 风速
humidity = weather_resp.json()['now']['humidity'] # 湿度
precip = weather_resp.json()['now']['precip'] # 降水量
pressure = weather_resp.json()['now']['pressure'] # 大气压强
vis = weather_resp.json()['now']['vis'] # 能见度
cloud = weather_resp.json()['now']['cloud'] # 云量
dew = weather_resp.json()['now']['dew'] # 露点温度

# 发送到bark
key = "UZ9juRSNtAMpnzWEQokJYF"
show_time = update_time.split("+")[0].replace("T", " ")
title = f"{show_time}"
test = "/"
content = f"""
🌐地点: 上海-浦东新区

✅天气: {text}✅温度: {temp}°C✅体感温度: {feels_like}°C

✅风向: {wind_dir}✅风力: {wind_scale}级✅风速: {wind_speed}km

✅湿度: {humidity}%✅降水量: {precip}mm

❎信息来源: 和风天气api
"""
bark = SendBark(key)
bark.send_t_c(title, content)