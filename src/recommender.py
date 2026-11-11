import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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
    """Load songs from a CSV into a list of dicts, converting numeric fields to int/float."""
    int_fields = ("id", "tempo_bpm")
    float_fields = ("energy", "valence", "danceability", "acousticness")

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded {len(songs)} songs from {csv_path}")
    return songs

# Scoring weights (10-point max). Edit these to run weight experiments.
CATEGORICAL_WEIGHTS = {"mood": 3.0, "genre": 2.0}
NUMERIC_WEIGHTS = {"energy": 2.0, "valence": 1.0, "acousticness": 1.0, "danceability": 1.0}

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences (max 10), returning (score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    for feature, points in CATEGORICAL_WEIGHTS.items():
        target = user_prefs.get(feature)
        if target is not None and str(song[feature]).lower() == str(target).lower():
            score += points
            reasons.append(f"{feature} match (+{points:.1f})")

    for feature, max_points in NUMERIC_WEIGHTS.items():
        target = user_prefs.get(feature)
        if target is None:
            continue
        closeness = max(0.0, 1.0 - abs(song[feature] - target))
        earned = max_points * closeness
        score += earned
        reasons.append(
            f"{feature} {song[feature]:.2f} vs target {target:.2f} (+{earned:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k as (song, score, explanation), best first."""
    target_energy = user_prefs.get("energy")

    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        energy_gap = abs(song["energy"] - target_energy) if target_energy is not None else 0.0
        scored.append((song, score, "; ".join(reasons), energy_gap))

    scored.sort(key=lambda item: (-item[1], item[3], item[0]["title"]))
    return [(song, score, explanation) for song, score, explanation, _ in scored[:k]]
