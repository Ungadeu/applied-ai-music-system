import logging
from recommender import load_songs, recommend_songs, calculate_score, get_explanation

# 1. The "Diary" setup
logging.basicConfig(filename='system.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_input():
    print("\n🎧 Welcome to the AI Vibe Curator! 🎧")
    print("Let's build your custom writing playlist.\n")
    
    # 1. Ask for Genre
    genre_ans = input("What genre are you looking for? (e.g., pop, lofi, rock, ambient): ")
    # Clean up the text and put it in a list
    genres = [genre_ans.strip().lower()] if genre_ans else ["lofi"] 
    
    # 2. Ask for Mood
    mood_ans = input("What mood do you need? (e.g., happy, chill, intense, peaceful): ")
    moods = [mood_ans.strip().lower()] if mood_ans else ["chill"]
    
    # 3. Ask for Energy (with error handling so it doesn't crash!)
    energy_ans = input("How much energy do you need? (0.0 for asleep, 1.0 for sprinting): ")
    try:
        energy = float(energy_ans)
    except ValueError:
        print("  -> Whoops, that wasn't a number! We will default to medium energy (0.5).")
        energy = 0.5
        
    print("\nAnalyzing catalog and retrieving context...\n")
    
    # Package it all up into the dictionary your AI expects
    return {
        "favorite_genres": genres,
        "favorite_moods": moods,
        "target_energy": energy,
        "target_valence": 0.5,        # Defaulting these so the math doesn't break
        "target_acousticness": 0.5,
        "target_danceability": 0.5
    }

def main() -> None:
    logging.info("System Started. Loading songs...")
    
    try:
        songs = load_songs("data/songs.csv") 
        logging.info(f"Successfully loaded {len(songs)} songs.")
    except Exception as e:
        # If it crashes (e.g., missing file), write it in the diary!
        logging.error(f"Failed to load songs! Error: {e}")
        return # Stop the program if we can't load songs    

    # Starter example profile
    user_profile = {"favorite_genres": ["pop"], "favorite_moods": ["happy"], "target_energy": 0.8, "likes_acoustic": False}
    logging.info(f"Generating recommendations for profile: {user_profile['favorite_genres']}")

    Recommender = recommend_songs(user_profile, songs, k=5)
    

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
        
        # Log the success!
        logging.info(f"Recommended: {song['title']} (Score: {score})")
    logging.info("System finished successfully.\n")    

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
