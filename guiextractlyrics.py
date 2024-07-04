import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Function to fetch lyrics using Genius.com API
def fetch_lyrics():
    artist = entry_artist.get().strip()
    song = entry_song.get().strip()
    
    if not artist or not song:
        messagebox.showwarning("Missing Information", "Please enter both artist and song name")
        return
    
    try:
        genius = lyricsgenius.Genius('YOUR_GENIUS_API_TOKEN_HERE')  # Replace with your Genius API token
        song_lyrics = genius.search_song(song, artist).lyrics
        
        # Display lyrics in the text area
        text_output.delete(1.0, tk.END)  # Clear previous text
        text_output.insert(tk.END, song_lyrics)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch lyrics:\n{str(e)}")

# Create the main window
root = tk.Tk()
root.title("Song Lyrics Extractor")

# Create labels and entry boxes for artist and song input
label_artist = tk.Label(root, text="Artist:")
label_artist.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_artist = tk.Entry(root, width=50)
entry_artist.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

label_song = tk.Label(root, text="Song:")
label_song.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_song = tk.Entry(root, width=50)
entry_song.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Create a button to fetch lyrics
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=1, pady=15)

# Create a text area to display lyrics
text_output = tk.Text(root, wrap=tk.WORD, width=60, height=20)
text_output.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Run the main event loop
root.mainloop()
