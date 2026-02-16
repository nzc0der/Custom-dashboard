if application "Spotify" is running then
	tell application "Spotify"
		set isPlaying to player state as string
		set trackName to name of current track
		set artistName to artist of current track
		set albumName to album of current track
		set artUrl to artwork url of current track
		return isPlaying & "|" & trackName & "|" & artistName & "|" & albumName & "|" & artUrl
	end tell
else
	return "stopped||||"
end if
