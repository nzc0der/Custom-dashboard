import axios from 'axios';

const API_KEY = ''; // User should provide this
const USERNAME = 'johndoe'; // User should provide this
const BASE_URL = 'https://ws.audioscrobbler.com/2.0/';

export const fetchNowPlaying = async () => {
  if (!API_KEY) {
    // Return mock data if no API key is provided
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          isPlaying: true,
          track: 'Starboy',
          artist: 'The Weeknd',
          album: 'Starboy',
          image: 'https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?q=80&w=200&h=200&auto=format&fit=crop',
        });
      }, 1500);
    });
  }

  try {
    const response = await axios.get(BASE_URL, {
      params: {
        method: 'user.getrecenttracks',
        user: USERNAME,
        api_key: API_KEY,
        format: 'json',
        limit: 1,
      },
    });

    const track = response.data.recenttracks.track[0];
    const isPlaying = track['@attr'] && track['@attr'].nowplaying === 'true';

    return {
      isPlaying,
      track: track.name,
      artist: track.artist['#text'],
      album: track.album['#text'],
      image: track.image[track.image.length - 1]['#text'],
    };
  } catch (error) {
    console.error('Error fetching music:', error);
    throw error;
  }
};
