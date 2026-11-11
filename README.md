# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend
You can include a simple diagram or bullet list if helpful.

Real-world platforms like Spotify and YouTube predict what you'll love next by combining several signals. They use collaborative filtering (what similar users played, skipped, or saved) and content-based filtering (the attributes of the songs themselves). A candidate stage narrows millions of songs down, and a ranking stage orders what's left. My version is a simple content-based recommender, so it can only use song attributes and a single user's stated taste, not other users' behavior. It scores each song by how close its energy is to the user's target, instead of rewarding higher or lower values. It gives a mood match more weight than a genre match, since genre is sparse in the small catalog. It also lets acousticness matter more when the user wants high-energy music. A separate ranking step then sorts the scored songs and returns the top k, with reasons attached. Prioritizing explainability and closeness over raw popularity means it can't discover surprising tastes the way collaborative filtering can. In exchange, every recommendation can be traced back to specific features.


Feature	Points	Type
Mood	3	exact match
Genre	2	exact match
Energy	2	proximity
Valence	1	proximity
Acousticness	1	proximity
Danceability	1	proximity
Total	10	
The ratios are the same as before: mood is 1.5× genre, and the four numeric features together carry 5 of the 10 points.

Proximity scoring: points = max_points × (1 − |song_value − target_value|), so a 1-point feature can give a fractional score such as 0.85. Keep the decimals and round only when displaying.
Sample scores: a mood and genre match with close numerics scores about 8–9.5. A mood-only match with close numerics scores about 6.5–7.5. A genre-only match with a wrong mood scores about 4.5–5.5.
Genre-weight experiment: with these integer weights, halving genre means 2 → 1 and doubling energy means 2 → 4. The total then becomes 11, so also drop mood to 2, or normalize by dividing by the sum of the weights.

Might over prioritize mood and might make danceablity too far from energy (even tho kind of similar)
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: 
============================================================
                    TOP RECOMMENDATIONS                     
         Profile: genre=pop, mood=happy, energy=0.8         
============================================================

#1  Sunrise City  -  Neon Echo
    Score: 6.96 / 10
    Why:
      - mood match (+3.0)
      - genre match (+2.0)
      - energy 0.82 vs target 0.80 (+1.96)
------------------------------------------------------------

#2  Una Noche en Medellín  -  Cris MJ
    Score: 4.96 / 10
    Why:
      - mood match (+3.0)
      - energy 0.78 vs target 0.80 (+1.96)
------------------------------------------------------------

#3  Rooftop Lights  -  Indigo Parade
    Score: 4.92 / 10
    Why:
      - mood match (+3.0)
      - energy 0.76 vs target 0.80 (+1.92)
------------------------------------------------------------

#4  Free Your Mind  -  Prospa
    Score: 4.84 / 10
    Why:
      - mood match (+3.0)
      - energy 0.88 vs target 0.80 (+1.84)
------------------------------------------------------------

#5  Gym Hero  -  Max Pulse
    Score: 3.74 / 10
    Why:
      - genre match (+2.0)
      - energy 0.93 vs target 0.80 (+1.74)
------------------------------------------------------------

============================================================
               Edge 1: high energy + sad mood               
               Profile: energy=0.9, mood=sad                
============================================================

#1  Storm Runner  -  Voltline
    Score: 1.98 / 10
    Why:
      - energy 0.91 vs target 0.90 (+1.98)
------------------------------------------------------------

#2  Free Your Mind  -  Prospa
    Score: 1.96 / 10
    Why:
      - energy 0.88 vs target 0.90 (+1.96)
------------------------------------------------------------

#3  Gym Hero  -  Max Pulse
    Score: 1.94 / 10
    Why:
      - energy 0.93 vs target 0.90 (+1.94)
------------------------------------------------------------

#4  Iron Tide  -  Black Harbor
    Score: 1.86 / 10
    Why:
      - energy 0.97 vs target 0.90 (+1.86)
------------------------------------------------------------

#5  Sunrise City  -  Neon Echo
    Score: 1.84 / 10
    Why:
      - energy 0.82 vs target 0.90 (+1.84)
------------------------------------------------------------

============================================================
                 Edge 3: unknown genre/mood                 
            Profile: genre=k-pop, mood=ecstatic             
============================================================

#1  4Me 4Me  -  Malcolm Todd
    Score: 0.00 / 10
    Why:
      - no matching preferences (score 0.0)
------------------------------------------------------------

#2  Coffee Shop Stories  -  Slow Stereo
    Score: 0.00 / 10
    Why:
      - no matching preferences (score 0.0)
------------------------------------------------------------

#3  Drama  -  Bizzey
    Score: 0.00 / 10
    Why:
      - no matching preferences (score 0.0)
------------------------------------------------------------

#4  Dust Road Sunday  -  Hollis Creek
    Score: 0.00 / 10
    Why:
      - no matching preferences (score 0.0)
------------------------------------------------------------

#5  Focus Flow  -  LoRoom
    Score: 0.00 / 10
    Why:
      - no matching preferences (score 0.0)
------------------------------------------------------------

============================================================
        Edge 10: likes_acoustic vs acousticness 0.0         
       Profile: likes_acoustic=True, acousticness=0.0       
============================================================

#1  Iron Tide  -  Black Harbor
    Score: 0.97 / 10
    Why:
      - acousticness 0.03 vs target 0.00 (+0.97)
------------------------------------------------------------

#2  Free Your Mind  -  Prospa
    Score: 0.96 / 10
    Why:
      - acousticness 0.04 vs target 0.00 (+0.96)
------------------------------------------------------------

#3  Gym Hero  -  Max Pulse
    Score: 0.95 / 10
    Why:
      - acousticness 0.05 vs target 0.00 (+0.95)
------------------------------------------------------------

#4  Pretty Green Eyes  -  KETTAMA
    Score: 0.94 / 10
    Why:
      - acousticness 0.06 vs target 0.00 (+0.94)
------------------------------------------------------------

#5  Drama  -  Bizzey
    Score: 0.90 / 10
    Why:
      - acousticness 0.10 vs target 0.00 (+0.90)
------------------------------------------------------------
---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



