import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';

const Clock = () => {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (date) => {
    return date.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: true,
    });
  };

  const formatDate = (date) => {
    return date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  };

  const getGreeting = () => {
    const hour = time.getHours();
    if (hour < 12) return 'Good Morning';
    if (hour < 18) return 'Good Afternoon';
    return 'Good Evening';
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="flex flex-col items-center justify-center p-8 glass rounded-3xl"
    >
      <motion.h2
        className="text-2xl font-light tracking-widest text-blue-200 uppercase"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
      >
        {getGreeting()}
      </motion.h2>
      <motion.h1
        className="mt-2 text-8xl font-bold tracking-tighter text-white"
        layout
      >
        {formatTime(time).split(' ')[0]}
        <span className="text-4xl ml-2 font-medium opacity-80">
          {formatTime(time).split(' ')[1]}
        </span>
      </motion.h1>
      <motion.p
        className="mt-4 text-xl font-medium text-blue-100/70"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.7 }}
      >
        {formatDate(time)}
      </motion.p>
    </motion.div>
  );
};

export default Clock;
