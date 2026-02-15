import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Cloud, Sun, CloudRain, Wind, Droplets, RefreshCw } from 'lucide-react';
import { fetchWeather } from '../services/weatherService';

const Weather = () => {
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const getWeatherData = async () => {
    setLoading(true);
    try {
      const data = await fetchWeather();
      setWeather(data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch weather');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getWeatherData();
    const interval = setInterval(getWeatherData, 600000); // Update every 10 mins
    return () => clearInterval(interval);
  }, []);

  const getWeatherIcon = (condition) => {
    const iconClass = "w-12 h-12 text-blue-300";
    switch (condition) {
      case 'Clear': return <Sun className={iconClass} />;
      case 'Clouds': return <Cloud className={iconClass} />;
      case 'Rain': return <CloudRain className={iconClass} />;
      default: return <Cloud className={iconClass} />;
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      className="p-6 glass rounded-3xl min-w-[300px]"
    >
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-semibold text-white/90">Weather</h3>
        <button
          onClick={getWeatherData}
          className="p-2 transition-colors rounded-full hover:bg-white/10"
        >
          <RefreshCw className={`w-4 h-4 text-white/50 ${loading ? 'animate-spin' : ''}`} />
        </button>
      </div>

      <AnimatePresence mode="wait">
        {loading && !weather ? (
          <motion.div
            key="loading"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="flex items-center justify-center h-32"
          >
            <div className="w-8 h-8 border-t-2 border-blue-400 rounded-full animate-spin"></div>
          </motion.div>
        ) : weather ? (
          <motion.div
            key="content"
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="space-y-4"
          >
            <div className="flex items-center space-x-4">
              {getWeatherIcon(weather.condition)}
              <div>
                <div className="text-4xl font-bold text-white">{weather.temp}°C</div>
                <div className="text-lg text-blue-100/60">{weather.condition}</div>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4 pt-4 border-t border-white/10">
              <div className="flex items-center space-x-2">
                <Wind className="w-4 h-4 text-blue-300/70" />
                <span className="text-sm text-white/80">{weather.windSpeed} km/h</span>
              </div>
              <div className="flex items-center space-x-2">
                <Droplets className="w-4 h-4 text-blue-300/70" />
                <span className="text-sm text-white/80">{weather.humidity}%</span>
              </div>
            </div>
            <div className="text-xs text-center text-white/30 uppercase tracking-widest pt-2">
              {weather.city}
            </div>
          </motion.div>
        ) : (
          <motion.div
            key="error"
            className="text-red-400 text-center py-8"
          >
            {error}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

export default Weather;
