# 📑 Model Card & Ethics Reflection

This document outlines the ethical considerations, technical limitations, and collaborative journey involved in building the **AI Vibe Curator**.

---

### ⚖️ System Limitations & Biases

Every AI system has "blind spots," and this project identified two major ones:

* **The "Sticker" Bias**: Because the scoring logic grants a massive **+50 bonus** for genre matches, the system often ignores the actual "vibe" or energy of the music in favor of the label. This can lead to recommending intense metal songs to a user who specifically asked for quiet, low-energy background noise.
* **Data Scarcity**: With a catalog of only **18 songs**, the system cannot provide true variety. It effectively "ghosts" users whose specific niche tastes aren't represented, leading to a "Filter Bubble" where the same few tracks win every time.
* **Technical Simplicity**: The model assumes music can be reduced to a 0.0–1.0 scale. It misses human elements like lyrical depth, cultural significance, or the specific "vocal texture" of a singer.

---

### 🛡️ Misuse & Prevention

**Potential Misuse:** A developer might try to use this "toy" algorithm for a real commercial app. Because the math is tuned for a small classroom dataset, it would perform poorly on a library of millions of songs, likely recommending the same 1% of tracks over and over.

**Prevention Strategies:**
* **Transparency (RAG)**: By including the **Contextual Explainer**, I ensure the user knows exactly why a song was picked, which prevents them from feeling "manipulated" by an invisible algorithm.
* **Developer Guardrails**: The integrated **Logging** and **Test Suite** act as a safety net, warning future developers if an update breaks the "Ghost User" or "Conflicting Vibe" logic.

---

### 🧪 Reliability Surprises

During testing, I was surprised by how a **NameError** could reveal a deeper logic flaw. While troubleshooting why `top_songs` wasn't defined, I realized that the way the AI "unpacks" a recommendation bundle (Song + Score + Reasons) is incredibly fragile. One small change in how data is grouped can completely break the user-facing explanation, highlighting that reliability in AI isn't just about the math—it's about how the data flows through the pipes.

---

### 🤝 AI Collaboration Reflection

Working with AI to build this system was a balanced partnership of creative planning and technical correction:

* **The Helpful Suggestion**: The AI suggested the **"Agentic Loop"** to solve the Sticker Bias. This idea of a system "checking its own work" and adjusting its weights if the score wasn't high enough transformed the project from a static script into a dynamic AI system.
* **The Flawed Suggestion**: During the final integration, the AI suggested code using a variable named `top_songs`. However, my local project was actually using the name `recommendations`. This caused a **NameError** that initially stopped the program. This served as a reminder that as an engineer, I must always verify that AI suggestions match my specific "codebase context".

---

### ✍️ What This Project Says About Me as an AI Engineer

This project reflects my dual identity as both a **Creative Writer** and a **Software Engineering Student**. It shows that I am an engineer who values **Transparency over Complexity**. I am not satisfied with a system that just "works"; I want a system that can explain itself to the user. By prioritizing the **RAG Contextual Explainer**, I demonstrated a commitment to building "Responsible AI" that respects the user's intelligence and helps them understand the mathematical decisions happening behind the scenes. It proves I am an engineer who builds with empathy for the end-user's creative flow.
