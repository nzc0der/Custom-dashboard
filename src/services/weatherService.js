import axios from 'axios';

const API_KEY = ''; // User should provide this
const BASE_URL = 'https://api.openweathermap.org/data/2.5';

export const fetchWeather = async (city = 'London') => {
  if (!API_KEY) {
    // Return mock data if no API key is provided
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          temp: 22,
          condition: 'Cloudy',
          icon: '04d',
          city: 'Mock City',
          humidity: 45,
          windSpeed: 12,
        });
      }, 1000);
    });
  }

  try {
    const response = await axios.get(`${BASE_URL}/weather`, {
      params: {
        q: city,
        appid: API_KEY,
        units: 'metric',
      },
    });

    return {
      temp: Math.round(response.data.main.temp),
      condition: response.data.weather[0].main,
      icon: response.data.weather[0].icon,
      city: response.data.name,
      humidity: response.data.main.humidity,
      windSpeed: response.data.wind.speed,
    };
  } catch (error) {
    console.error('Error fetching weather:', error);
    throw error;
  }
};
