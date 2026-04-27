"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs, calculate_score, get_explanation


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"favorite_genres": ["pop"], "favorite_moods": ["happy"], "target_energy": 0.8, "likes_acoustic": False}

    Recommender = recommend_songs(user_prefs, songs, k=5)
    

    print(f"Loaded songs: {len(songs)}")
    print("\n🎵 Top Music Recommendations 🎵\n")
    print("-" * 60)
    
    # We use 'recommendations' instead of 'top_songs' here
    for i, rec in enumerate(Recommender[:3], 1):
        # Your system bundles 3 things together, so we unpack them here:
        song, score, old_reasons = rec
        
        # Call our new AI Retriever tool from the encyclopedia
        smart_reason = get_explanation(song, round(score, 2))
        
        # Print it to the screen
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   {smart_reason}\n")


if __name__ == "__main__":
    main()

# main.py

# 1. High-Energy Pop: For active, upbeat sessions
high_energy_pop = {
    "favorite_genres": ["pop", "electronic"],
    "favorite_moods": ["happy", "energetic", "uplifting"],
    "target_energy": 0.90,
    "target_valence": 0.85,
    "target_acousticness": 0.10,
    "target_danceability": 0.85
}

# 2. Chill Lofi: Perfect for writing and focused studying
chill_lofi = {
    "favorite_genres": ["lofi", "ambient", "jazz"],
    "favorite_moods": ["chill", "focused", "peaceful"],
    "target_energy": 0.35,
    "target_valence": 0.50,
    "target_acousticness": 0.80,
    "target_danceability": 0.40
}

# 3. Deep Intense Rock: For high-stakes story moments
intense_rock = {
    "favorite_genres": ["rock", "metal"],
    "favorite_moods": ["intense", "dark", "moody"],
    "target_energy": 0.95,
    "target_valence": 0.30,
    "target_acousticness": 0.05,
    "target_danceability": 0.50
}
