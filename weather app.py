import tkinter as tk
from tkinter import scrolledtext
import requests

def fetch_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change the units to imperial if you prefer Fahrenheit
    }

    # Make the API call
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather():
    city_name = city_entry.get()
    api_key = '13f4d0cf97dc3138f8cc587c637414b7'  # Replace with your API key

    weather_data = fetch_weather(city_name, api_key)

    if weather_data:
        main_info = weather_data['main']
        temperature = main_info['temp']
        feels_like = main_info['feels_like']
        humidity = main_info['humidity']
        description = weather_data['weather'][0]['description']

        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        
        result_text.insert(tk.END, f"Weather in {city_name}:     \n", )
        result_text.insert(tk.END, f"Temperature:       {temperature} °C\n")
        result_text.insert(tk.END, f"Feels like:        {feels_like} °C\n")
        result_text.insert(tk.END, f"Humidity:          {humidity}%\n")
        result_text.insert(tk.END, f"Description:       {description}\n")
        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Weather data not available.")
        result_text.config(state=tk.DISABLED)

def create_window():
    # Create main window
    root = tk.Tk()
    root.title("Weather Information")
    root.geometry("400x300")
    root.configure(bg="#f0f7fb")  # Pastel blue background color

    # City entry
    city_label = tk.Label(root, text="Enter your city name:", bg="#f0f7fb")
    city_label.pack(pady=10)
    global city_entry
    city_entry = tk.Entry(root, width=30)
    city_entry.pack()

    # Fetch weather button
    fetch_button = tk.Button(root, text="Fetch Weather", command=display_weather)
    fetch_button.pack(pady=10)

    # Result display
    global result_text
    result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Courier New", 10))
    result_text.pack(padx=20, pady=20)
    result_text.config(state=tk.DISABLED)

    root.mainloop()

if __name__ == "__main__":
    create_window()

