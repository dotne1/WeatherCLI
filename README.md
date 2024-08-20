# WeatherCLI

A simple command-line tool for fetching and displaying weather information for any city.


## Table of Contents


- [Description](#description)

- [Installation](#installation)

- [Usage](#usage)

- [API Key](#api-key)

- [Requirements](#requirements)

- [Contributing](#contributing)

- [License](#license)

- [Acknowledgements](#acknowledgements)


## Description


`WeatherCLI` is a Python script designed to interact with the OpenWeatherMap API to retrieve current weather conditions for any given city. This tool is perfect for those who prefer command-line interfaces or want to integrate weather data into their scripts or applications.


## Installation


1. **Clone the Repository:**

   ```bash

   git clone git@github.com:dotne1/WeatherCLI.git

   cd WeatherCLI

2. **Install Dependencies:**
   ```bash

   pip install -r requirements.txt

## Usage

1. **Set your OpenWeatherMap API key as an environment variable:**

   ```bash

   export OPENWEATHER_API_KEY="your_api_key_here"

2. **Run the script:**

   ```bash

   python WeatherCLI.py <city_name>

3. **OR for GUI Feature**

   ```bash

   python WeatherGUI.py


## API Key

1. **OpenWeatherMap API Key:**
   You need to sign up for an API key from OpenWeatherMap. Ensure you keep your API key secure and do not commit it to your repository.

## Requirements

1. **Python 3.6+**
2. **requests library**

## Contributing

1. **Fork the repository.**
2. **Create a new branch (git checkout -b feature/awesome-feature).**
3. **Make your changes**
4. **Commit your changes (git commit -m 'Add some awesome feature').**
5. **Push to branch (git push origin feature/awesome-feature).**
6. **Create a Pull Request.**

## License

This project is licensed under the MIT License.

## Acknowledgements

1. **OpenWeatherMap for providing the weather data API.**
2. **Python Requests Library for making HTTP requests easy.**
