# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Vibezically**

---

## 2. Intended Use  

This recommender suggests songs from a small catalog. It picks the top 5 songs that fit what a listener asks for.

It assumes the listener can describe their taste. They give a mood, a genre, and numbers for energy and sound. It assumes one taste at a time, not a mix.

It is for classroom exploration. It is not for real users.

**Not for:** real music apps, or any choice that matters. The catalog is tiny. The scoring is simple. It can return bad matches without any warning.

---

## 3. How the Model Works  

Think of the recommender as a judge at a talent show. Every song gets points for how well it fits what the listener asked for. The highest scores are recommended.

The listener picks a mood and genre. They can also describe the sound they want: energy, upbeat feel, acoustic feel and danceability. Anything they leave out isn't judged.

Each song earns points like this:

- **Energy, up to 4 points:** the closer to what the listener wants, the more points.
- **Mood, up to 3 points:** all or nothing.
- **Genre, up to 1 point:** all or nothing.
- **Upbeat feel, acoustic sound and danceability, up to 1 point each:** scored by closeness, like energy.

The most points a song can earn is 11. The points are added up. Ties go to the song with the closer energy. Each recommendation also lists where its points came from, such as "mood match (+3.0)". That way you can see why it was picked.

**Change from the starter:** the starter only had empty placeholders. I added reading the song list, the scoring above, and ranking with readable reasons. I later doubled energy and halved genre as an experiment.

---

## 4. Data  

The catalog is a CSV file with 20 songs. Each song has a title, artist, genre, mood, energy, tempo, valence (upbeat feel), danceability and acousticness.

- **Genres:** 18 different ones. Lofi has 3 songs and pop has 2. The rest have 1 each.
- **Moods:** happy, chill, intense, relaxed, moody and focused. There is no "sad".
- **Not used:** tempo is in the data but the scoring ignores it.

The catalog is small and leans toward low-energy songs. It is missing a lot of taste: sad music, most world genres, and any song with lyrics or language info. I did not change the data during testing.

---

## 5. Strengths  

- It works well when the listener's taste matches songs that exist. The pop and happy profile returned Sunrise City first, which felt right.
- The reasons are easy to read. You can see which features gave points.
- Closeness scoring is fair for numbers. A song that is a little off still gets most of the points.
- A perfect match to one song scores the full 11, so the math checks out.

---

## 6. Limitations and Bias 

- **Lofi bubble.** Seven of 20 songs have energy at or below 0.45, and lofi has the most songs. In 2,000 random profiles, the 3 lofi songs were in the top 5 for 43% to 51% of listeners. The same songs show up for almost everyone.
- **Niche tastes lose.** Listeners who like metal, hip hop or regional Mexican have only one or two songs that can fit them.
- **Exact matching.** "Indie pop" and "bedroom pop" get no credit for "pop". A "sad" mood matches nothing.
- **Silent failure.** An unknown genre and mood gave every song a score of 0. The list was just alphabetical. The user gets no warning.
- **Ignored input.** `likes_acoustic` is never read. Tempo is never used.
- **One target per feature.** A listener who likes both calm and loud songs can't say so.

---

## 7. Evaluation  

**Profiles tested:** Starter (pop, happy, energy 0.8), Edge 1 (energy 0.9, mood sad), Edge 3 (unknown genre "k-pop" and mood "ecstatic"), Edge 10 (likes_acoustic True but acousticness 0.0).

**What surprised me:** The scores were low. The best was 7.92 out of 11, and the edge profiles scored 0 to 4. A profile can only earn points for features it specifies, so a short profile can never look like a strong match. The raw score shows how much the user told us more than how well the songs fit.

**Pairwise comparisons:**
- **Starter vs Edge 1:** Starter returns happy, mid-to-high energy songs (Sunrise City, 7.92). Edge 1 returns high-energy songs that aren't sad (Storm Runner, 3.96). This makes sense because the catalog has no "sad" songs, so only energy shaped the ranking.
- **Starter vs Edge 3:** Starter finds clear matches. Edge 3 asks for values that don't exist, so every song scores 0 and the list is alphabetical. That's valid for exact matching but misleading to a user.
- **Starter vs Edge 10:** Starter surfaces happy pop. Edge 10 returns the least acoustic songs (Iron Tide, Free Your Mind), the opposite of what "likes acoustic" implies, because `likes_acoustic` is never read.
- **Edge 1 vs Edge 3:** Edge 1 has an energy target, so it still produces a meaningful ranking even though its mood fails. Edge 3 has no numeric target, so nothing can score. One numeric preference is what keeps results useful when categories miss.
- **Edge 1 vs Edge 10:** Both are ranked by numeric closeness only. Edge 1 favors loud, high-energy songs (Storm Runner, Iron Tide) and Edge 10 favors non-acoustic songs (Iron Tide, Free Your Mind). They overlap because loud songs tend to be non-acoustic, which makes sense.
- **Edge 3 vs Edge 10:** Edge 3 scores every song 0 because its categories don't exist. Edge 10 scores every song above 0.9 because acousticness is a numeric feature that always gives partial credit. So exact-match categories can fail completely, while numeric features never do.

**Weight-shift test:** Doubling energy and halving genre didn't change the order for these profiles, since none puts genre and energy in conflict. A profile of pop with energy 0.4 did change: pop songs ranked first before, and lofi songs rank first after.

**Other checks:** I ran 2,000 random profiles to look for bias. The 2 existing tests still pass.

---

## 8. Future Work  

- **Fix the scores.** Divide by the most points the profile could earn, so short and long profiles can be compared.
- **Use genre families.** Let "indie pop" and "bedroom pop" earn partial credit for "pop". Add songs for missing moods like "sad".
- **Warn the user.** Say so when nothing matches, and use `likes_acoustic`.
- **Add variety.** Mix up the top 5 so the same lofi songs don't fill every list.

---

## 9. Personal Reflection  

**Biggest learning moment:** Working code can still give biased results. The same lofi songs showed up for almost everyone.

**AI help and double-checking:** AI helped me write the scoring and find edge cases. But it predicted that "sad" would beat energy, and that was wrong. The catalog has no sad songs. I had to check claims against the real data.

**What surprised me:** A few added points still felt like a real recommendation. But odd profiles still got confident-looking lists.

**What I'd try next:** Normalize the scores, add genre families and more songs, and mix up the top 5.
