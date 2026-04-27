🎧 Vibe Curator: RAG-Enhanced Music Recommender
📝 Project Summary
The AI Vibe Curator is an interactive music recommendation system designed to help creative writers find the perfect background "vibe" for their storytelling sessions. By combining mathematical proximity scoring with Retrieval-Augmented Generation (RAG), the system doesn't just suggest a song—it retrieves cultural and technical context from a specialized knowledge base to explain why that specific track fits your creative goals.

🛠️ Based on Original Project
This project is an evolution of ai110-module3show-musicrecommendersimulation-starter.

Original Goals: The starter project was a basic simulation focused on demonstrating how mathematical proximity scoring can predict user preferences within a small, static catalog.

Capabilities: It handled fundamental genre/mood matching and provided simple numerical rankings for a fixed user profile.

🏗️ Architecture Overview
The system follows an Input → Process → Retrieve → Output workflow:

User Input: An interactive questionnaire captures the user's desired genre, mood, and energy level.

Scoring Engine: The core algorithm calculates points based on Genre (+50), Mood (+40), and Numerical Proximity (+60).

RAG Retriever: Once a top song is identified, the system queries the music_knowledge.py library to find the matching genre "encyclopedia" entry.

Explainer: The system merges the score and the retrieved context into a transparent justification for the user.

🚀 Setup Instructions
To run the AI Vibe Curator on your local machine using Visual Studio Code and a zsh terminal:

Clone the project and ensure your files (main.py, recommender.py, music_knowledge.py, songs.csv) are in the src/ folder.

Activate your environment:

Bash
source .venv/bin/activate
Install requirements:

Bash
pip install -r requirements.txt
Launch the Interactive Curator:

Bash
python src/main.py
🧪 Sample Interactions
Example 1: The Focused Author

Input: Genre: lofi, Mood: chill, Energy: 0.3.

Output: 1. Library Rain by LoRoom.

AI Explanation: "Score: 147.5/150. We picked this lofi track because: Lofi uses soft, repetitive beats and slightly muffled sounds... amazing for deep focus and creative writing".

Example 2: The Action Scene

Input: Genre: rock, Mood: intense, Energy: 0.9.

Output: 1. Thunder Strike by Max Pulse.

AI Explanation: "Score: 148.2/150. We picked this rock track because: Rock features strong drum beats and electric guitars... for high-stakes story moments".

🎨 Design Decisions & Trade-offs
Transparency over Speed: I chose to implement a RAG module rather than a simple printout of scores. While this adds a step to the processing, it makes the AI's "black box" decisions understandable to the end-user.

Weight Sensitivity: During development, I discovered a "Sticker Bias" where genre labels drowned out actual energy levels. I adjusted the weights to ensure numerical "vibe" (Energy/Valence) could effectively influence the ranking alongside categorical labels.

Small Catalog Constraint: The system is currently limited to 18 songs. This was a conscious trade-off to ensure 100% accuracy in the RAG retrieval logic before scaling to a larger database.

📊 Testing Summary
I implemented a specialized test_system.py script to ensure reliability across different user scenarios.

Results: 3 out of 3 tests passed.

Successes: The system successfully retrieved correct facts for known genres and, crucially, used a Reliability Guardrail to provide a backup message when an unknown genre was entered.

Lessons: Testing revealed that empty user profiles need clear default values to prevent mathematical "None" errors.

💡 Reflection: 
This project taught me that Applied AI is about more than just a clever algorithm; it’s about the relationship between data and the user. I learned that "optimal" math doesn't always equal a "good" recommendation if the user doesn't understand why a choice was made. Solving the "Sticker Bias" through weight adjustment and context retrieval showed me how to fine-tune AI behavior to better mimic human musical intuition.

Project Walkthrough Video Link:
https://www.loom.com/share/b972fc299e6346be9fe1573c7673c477
