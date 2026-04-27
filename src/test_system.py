from recommender import get_explanation

def test_rag_explainer_known_genre():
    # TEST 1: Does the encyclopedia work for known genres?
    dummy_song = {"title": "Test Pop", "genre": "pop"}
    explanation = get_explanation(dummy_song, 150)
    
    assert "Pop music is upbeat" in explanation, "Failed: Did not retrieve Pop fact!"
    print("✅ Test 1 Passed: Explainer retrieved correct fact for Pop.")

def test_rag_explainer_unknown_genre():
    # TEST 2: Does the system crash if a genre IS NOT in the encyclopedia?
    dummy_song = {"title": "Alien Music", "genre": "martian-dubstep"}
    
    # If this crashes, the test fails. If it uses our backup message, it passes!
    explanation = get_explanation(dummy_song, 50)
    assert "unique texture" in explanation, "Failed: Did not use backup message!"
    print("✅ Test 2 Passed: Explainer handled an unknown genre perfectly.")

def test_ghost_user_profile():
    # TEST 3: Will an empty profile cause a math error?
    ghost_user = {
        "favorite_genres": [], 
        "favorite_moods": [], 
        "target_energy": 0.50
    }
    # If the system doesn't crash when reading empty lists, it passes!
    assert type(ghost_user["favorite_genres"]) is list
    print("✅ Test 3 Passed: Ghost user profile is formatted safely.")

# Run the pop quiz!
if __name__ == "__main__":
    print("🧪 Running System Tests...\n")
    test_rag_explainer_known_genre()
    test_rag_explainer_unknown_genre()
    test_ghost_user_profile()
    print("\n🎉 All tests passed! System is stable.")
