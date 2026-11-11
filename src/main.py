"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs, MAX_SCORE


PROFILES = {
    "Starter (pop/happy)": {"genre": "pop", "mood": "happy", "energy": 0.8},
    # Adversarial / edge-case profiles
    "Edge 1: high energy + sad mood": {"energy": 0.9, "mood": "sad"},
    "Edge 3: unknown genre/mood": {"genre": "k-pop", "mood": "ecstatic"},
    "Edge 10: likes_acoustic vs acousticness 0.0": {
        "likes_acoustic": True,
        "acousticness": 0.0,
    },
}


def print_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    width = 60
    print("\n" + "=" * width)
    print(f"{name:^{width}}")
    print(
        f"{'Profile: ' + ', '.join(f'{key}={value}' for key, value in user_prefs.items()):^{width}}"
    )
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  -  {song['artist']}")
        print(f"    Score: {score:.2f} / {MAX_SCORE:g}")
        print("    Why:")
        for reason in explanation.split("; "):
            print(f"      - {reason}")
        print("-" * width)


def main() -> None:
    songs = load_songs("data/songs.csv")
    for name, prefs in PROFILES.items():
        print_recommendations(name, prefs, songs)


if __name__ == "__main__":
    main()
