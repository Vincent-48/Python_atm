import requests
from pythonosc import udp_client


# Function to search for music on YouTube and generate beats
def search_and_generate_beats(query):
    # Make an HTTP request to the YouTube API to search for videos matching the query.
    response = requests.get("https://www.googleapis.com/youtube/v3/search",
                            params={
                                "part": "snippet",
                                "q": query,
                                "type": "video",
                                "key": ""
                            })

    # Parse the response JSON to extract the video ID of the first result
    video_id = response.json()["items"][0]["id"]["videoId"]

    # Placeholder implementation to generate beats
    beats = [1, 0.5, 0.5, 1, 1, 0.5, 0.5, 1]

    return beats


# Set up the OSC client to communicate with Sonic Pi
client = udp_client.SimpleUDPClient("localhost", 4559)

# Example usage: Search for music and send beats to Sonic Pi
music_query = input("Enter the music title: ")
beats = search_and_generate_beats(music_query)

# Send the beats to Sonic Pi via OSC
for beat in beats:
    client.send_message("/play_beat", beat)
