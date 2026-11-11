# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
Vibezically

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Think of the recommender as a judge at a talent show. Every song gets marked out of 10 for how well it fits what the listener asked for, and the highest scores are recommended.

The listener picks a mood and genre and describes the sound they want: energy, upbeat feel, acoustic feel and danceability. Anything they leave out isn't judged.

Each song earns points like this:

- **Mood, up to 3 points:** all or nothing, and the most important match.
- **Genre, up to 2 points:** all or nothing.
- **Energy, up to 2 points:** the closer to what the listener wants, the more points.
- **Upbeat feel, acoustic sound and danceability, up to 1 point each:** scored by closeness, like energy.

The points are added up, and ties go to the song with the closer energy. Each recommendation also lists where its points came from, such as "mood match (+3.0)", so you can see why it was picked.

**Change from the starter:** the starter only had empty placeholders. I added reading the song list, the scoring above, and ranking with readable reasons.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
