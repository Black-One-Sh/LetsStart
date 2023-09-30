from aiogram import Bot, Dispatcher, executor, types
import requests
import json


#bot_init
bot = Bot(token="6028087461:AAFCcJWzTsy3dSzqDLOcEKBKww-tDVlbAjM")
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
	city = message.text
	url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')
	weather_data = requests.get(url).json()
	weather_data_structure = json.dumps(weather_data, indent=2)

	temperature = weather_data['main']['temp']
	temperature_feels = round(weather_data['main']['feels_like'])
	wind_speed = weather_data['wind']['speed']

	resp_msg = Ощущается, как temperature_feels, градусов.
	resp_msg1 = Скорость ветра, wind_speed, м/с.


	await message.answer(resp_msg)
	await message.answer(resp_msg1)

#run long-polling
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)