"""
@Time ： 2026/10/19 22:32
@Auth ： seven
@File ：工具调用.py
@IDE ：PyCharm
"""
async def weather_tool(params):
    city = params["city"]
    weather_data = {"北京":"今天北京的天气是25度"}
    if city in weather_data:
        return weather_data[city]

    raise Exception("工具调用异常")

