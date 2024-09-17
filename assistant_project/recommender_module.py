from sklearn.neighbors import NearestNeighbors
import numpy as np

def recommend_song(user_preferences, song_data):
    model = NearestNeighbors(n_neighbors=5)
    model.fit(song_data)
    distances, indices = model.kneighbors([user_preferences])
    return indices

song_data = np.array([
    [120, 1, 0, 0.8],  # Song 1
    [90, 2, 1, 0.6],   # Song 2
    [150, 1, 1, 0.9],  # Song 3
    [110, 3, 0, 0.7],  # Song 4
    [80, 2, 1, 0.5]    # Song 5
])

def get_mean_energy():
    mean_energy = np.mean(song_data[:, 3])

def get_highest_energy_song():
    highest_energy_index = np.argmax(song_data[:, 3])
    return highest_energy_index
