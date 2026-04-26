from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from music_knowledge import genre_explanations
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'valence': float(row['valence']),
                'acousticness': float(row['acousticness']),
                'danceability': float(row['danceability']),
                'tempo_bpm': int(row['tempo_bpm'])
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate the score for a song based on user preferences."""
    score = 0.0
    reasons = []
    
    # Genre match: +50 points
    if song['genre'] in user_prefs.get('favorite_genres', []):
        score += 50.0
        reasons.append("genre match (+50)")
    
    # Mood match: +40 points
    if song['mood'] in user_prefs.get('favorite_moods', []):
        score += 40.0
        reasons.append("mood match (+40)")
    
    # Energy proximity: 60 * (1 - |target_energy - song_energy|)
    energy_diff = abs(user_prefs['target_energy'] - song['energy'])
    energy_score = 60.0 * (1.0 - energy_diff)
    score += energy_score
    reasons.append(f"energy proximity (+{energy_score:.1f})")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Recommend top k songs based on user preferences."""
    scored_songs = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]

def calculate_score(song, profile):
    total_score = 0
    
    # 1. Categorical Matches
    # REDUCED: Genre is now worth half (25 points)
    if song['genre'] in profile['favorite_genres']:
        total_score += 25
    
    # Mood remains at its last finalized weight
    if song['mood'] in profile['favorite_moods']:
        total_score += 40
        
    # 2. Numerical Proximity Matches
    # DOUBLED: Energy is now worth 40 points
    energy_diff = abs(profile['target_energy'] - song['energy'])
    total_score += 40 * (1 - energy_diff)
    
    # Remaining texture weights stay the same
    total_score += 15 * (1 - abs(profile['target_valence'] - song['valence']))
    total_score += 15 * (1 - abs(profile['target_acousticness'] - song['acousticness']))
    total_score += 10 * (1 - abs(profile['target_danceability'] - song['danceability']))
    
    return total_score

    def get_explanation(song, score):
    # 1. Figures out what genre the song is
    song_genre = song['genre']
    
    # 2. Looks up the genre in our encyclopedia
    # If it's not available, use a backup message
    knowledge = genre_explanations.get(song_genre, "This genre has a unique texture that perfectly matches your current targets.")
    
    # 3. Combines the math score with the knowledge
    explanation = f"Score: {score}/150. We picked this {song_genre} track because: {knowledge}"
    
    return explanation
