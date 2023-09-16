import tkinter as tk

API_KEY = "481991d124506eeb6d0082fa0a88ebbd"

API_URL = "http://api.weatherstack.com/current"

root = tk.Tk()
root.title("Weather Forecast")

city_label = tk.Label(root, text="City:")
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=5, pady=5)

country_label = tk.Label(root, text="Country:")
country_label.grid(row=1, column=0, padx=5, pady=5)

country_entry = tk.Entry(root)
country_entry.grid(row=1, column=1, padx=5, pady=5)

def get_weather():
   city = city_entry.get()
   country = country_entry.get()
   url = f"{API_URL}?access_key={API_KEY}&query={city},{country}"
   response = requests.get(url).json()
   temperature = response["current"]["temperature"]
   weather_desc = response["current"]["weather_descriptions"][0]
   temperature_label.config(text=f"Temperature: {temperature}°C")
   weather_desc_label.config(text=f"Weather Description: {weather_desc}")

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

temperature_label = tk.Label(root, text="")
temperature_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

weather_desc_label = tk.Label(root, text="")
weather_desc_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
