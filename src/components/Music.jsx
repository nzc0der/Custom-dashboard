import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Music as MusicIcon, Play, Pause, Disc } from 'lucide-react';
import { fetchNowPlaying } from '../services/musicService';

const Music = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  const getMusicData = async () => {
    try {
      const result = await fetchNowPlaying();
      setData(result);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getMusicData();
    const interval = setInterval(getMusicData, 30000); // Update every 30s
    return () => clearInterval(interval);
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      className="p-6 glass rounded-3xl min-w-[350px]"
    >
      <div className="flex items-center space-x-2 mb-4">
        <MusicIcon className="w-5 h-5 text-pink-400" />
        <h3 className="text-xl font-semibold text-white/90">Currently Playing</h3>
      </div>

      <AnimatePresence mode="wait">
        {loading && !data ? (
          <motion.div
            key="loading"
            className="flex items-center justify-center h-24"
          >
             <Disc className="w-8 h-8 text-pink-500 animate-spin" />
          </motion.div>
        ) : data ? (
          <motion.div
            key="content"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="flex items-center space-x-6"
          >
            <div className="relative group">
              <motion.img
                src={data.image || 'https://via.placeholder.com/150'}
                alt="Album Art"
                className="w-24 h-24 rounded-2xl shadow-2xl object-cover"
                animate={{ rotate: data.isPlaying ? 360 : 0 }}
                transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
              />
              <div className="absolute inset-0 flex items-center justify-center bg-black/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity">
                {data.isPlaying ? <Pause className="w-8 h-8 text-white" /> : <Play className="w-8 h-8 text-white" />}
              </div>
            </div>

            <div className="flex-1 overflow-hidden">
              <h4 className="text-xl font-bold text-white truncate">{data.track}</h4>
              <p className="text-pink-200/70 font-medium truncate">{data.artist}</p>
              <p className="text-sm text-white/40 italic truncate">{data.album}</p>

              <div className="mt-3 flex items-center space-x-1">
                {[1, 2, 3, 4].map((i) => (
                  <motion.div
                    key={i}
                    className="w-1 bg-pink-500/60 rounded-full"
                    animate={{ height: data.isPlaying ? [8, 16, 8] : 4 }}
                    transition={{
                      duration: 0.8,
                      repeat: Infinity,
                      delay: i * 0.1,
                      ease: "easeInOut"
                    }}
                  />
                ))}
              </div>
            </div>
          </motion.div>
        ) : (
          <div className="text-white/30 text-center py-4 italic">Nothing playing right now</div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

export default Music;
