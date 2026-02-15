import React from 'react';
import { motion } from 'framer-motion';
import Clock from './components/Clock';
import Weather from './components/Weather';
import Music from './components/Music';
import ExtraInfo from './components/ExtraInfo';

function App() {
  return (
    <div className="relative min-h-screen w-full flex flex-col items-center justify-center p-4 md:p-8">
      {/* Background Decorative Elements */}
      <div className="absolute top-1/4 left-1/4 w-64 h-64 bg-blue-500/20 rounded-full blur-[120px] animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-[150px] animate-pulse delay-700" />

      <main className="relative z-10 w-full max-w-7xl mx-auto flex flex-col items-center gap-8 md:gap-12">
        {/* Top Section: Clock */}
        <div className="w-full flex justify-center">
          <Clock />
        </div>

        {/* Middle Section: Stats & Info Grid */}
        <div className="w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8 items-stretch">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="flex"
          >
            <Weather />
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4 }}
            className="flex lg:col-span-1"
          >
            <Music />
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.6 }}
            className="flex md:col-span-2 lg:col-span-1"
          >
            <ExtraInfo />
          </motion.div>
        </div>

        {/* Footer / Status Bar */}
        <motion.footer
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="w-full max-w-3xl mt-8 p-4 glass rounded-2xl flex items-center justify-between text-xs text-white/30 uppercase tracking-[0.2em]"
        >
          <span>System Operational</span>
          <div className="flex items-center space-x-4">
            <span>v1.0.0</span>
            <div className="w-2 h-2 bg-green-500 rounded-full animate-ping" />
          </div>
        </motion.footer>
      </main>
    </div>
  );
}

export default App;
