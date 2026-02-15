import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Quote, Sparkles } from 'lucide-react';

const quotes = [
  { text: "The only way to do great work is to love what you do.", author: "Steve Jobs" },
  { text: "Innovation distinguishes between a leader and a follower.", author: "Steve Jobs" },
  { text: "Your time is limited, so don't waste it living someone else's life.", author: "Steve Jobs" },
  { text: "Stay hungry, stay foolish.", author: "Steve Jobs" },
  { text: "The future belongs to those who believe in the beauty of their dreams.", author: "Eleanor Roosevelt" },
  { text: "Believe you can and you're halfway there.", author: "Theodore Roosevelt" },
  { text: "It does not matter how slowly you go as long as you do not stop.", author: "Confucius" },
  { text: "Everything you've ever wanted is on the other side of fear.", author: "George Addair" },
  { text: "Success is not final, failure is not fatal: it is the courage to continue that counts.", author: "Winston Churchill" },
  { text: "Hardships often prepare ordinary people for an extraordinary destiny.", author: "C.S. Lewis" },
];

const ExtraInfo = () => {
  const [quote, setQuote] = useState(quotes[0]);
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prev) => (prev + 1) % quotes.length);
    }, 10000); // Change quote every 10s
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    setQuote(quotes[index]);
  }, [index]);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="p-6 glass rounded-3xl max-w-md"
    >
      <div className="flex items-center space-x-2 mb-4">
        <Sparkles className="w-5 h-5 text-yellow-400" />
        <h3 className="text-xl font-semibold text-white/90">Daily Inspiration</h3>
      </div>

      <AnimatePresence mode="wait">
        <motion.div
          key={index}
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 1.05 }}
          transition={{ duration: 0.5 }}
          className="relative"
        >
          <Quote className="absolute -top-2 -left-2 w-8 h-8 text-white/5 opacity-20" />
          <p className="text-lg text-blue-100/80 italic leading-relaxed pl-6">
            "{quote.text}"
          </p>
          <div className="mt-4 text-right">
            <span className="text-sm font-bold text-blue-300 uppercase tracking-widest">
              — {quote.author}
            </span>
          </div>
        </motion.div>
      </AnimatePresence>
    </motion.div>
  );
};

export default ExtraInfo;
