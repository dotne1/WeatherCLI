import tkinter as tk
from tkinter import messagebox
from WeatherCLI import get_weather

def show_weather():
    city = entry.get()
    weather = get_weather(city)
    if weather:
        result_label.config(text=weather)
    else:
        messagebox.showerror("Error", "Couldn't fetch weather data for that city.")

# Main Window
root = tk.Tk()
root.title("Weather App - GUI Version")

# City Input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to fetch weather
fetch_button = tk.Button(root, text="Get Weather", command=show_weather)
fetch_button.pack(pady=5)

# Label to display weather
result_label = tk.Label(root, text="Enter a city name and click 'Get Weather'")
result_label.pack(pady=10)

root.mainloop()
