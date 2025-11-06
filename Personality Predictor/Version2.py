import tkinter as tk
from tkinter import scrolledtext, messagebox
import collections

def analyze_text(text):
    """
    Enhanced text analysis function to predict personality traits.
    Includes Big Five + Introversion/Extroversion, Confidence, Emotional Intelligence, Leadership, and Creativity.
    """
    trait_keywords = {
        'Openness': [
            'adventure', 'art', 'change', 'creative', 'curiosity', 'discover',
            'fantasy', 'ideas', 'imagine', 'innovation', 'intellectual', 'new',
            'philosophy', 'poetry', 'science', 'vision', 'abstract', 'complex'
        ],
        'Conscientiousness': [
            'achieve', 'ambition', 'attention', 'careful', 'control', 'detail',
            'discipline', 'duty', 'efficient', 'goal', 'hardworking', 'order',
            'organized', 'plan', 'prepare', 'reliable', 'responsible', 'schedule',
            'thorough', 'work'
        ],
        'Extraversion': [
            'active', 'assertive', 'attention', 'bold', 'chat', 'energetic',
            'enthusiasm', 'excitement', 'friends', 'gregarious', 'group', 'outgoing',
            'party', 'people', 'social', 'talkative', 'team', 'together', 'adventurous'
        ],
        'Agreeableness': [
            'altruism', 'care', 'charity', 'comfort', 'cooperate', 'empathy',
            'forgive', 'friendship', 'generous', 'help', 'kind', 'listen',
            'patience', 'peace', 'polite', 'share', 'sympathy', 'trust', 'warmth'
        ],
        'Neuroticism': [
            'anxiety', 'angry', 'depressed', 'fear', 'frustrated', 'insecure',
            'jealousy', 'moody', 'nervous', 'panic', 'sad', 'stress', 'vulnerable',
            'worry', 'anxious', 'doubt', 'overwhelmed'
        ],
        'Introversion': [
            'alone', 'quiet', 'reflective', 'reserved', 'thoughtful', 'solitude', 'independent', 'introspective', 'focus', 'contemplative'
        ],
        'Confidence': [
            'confident', 'belief', 'determined', 'courage', 'fearless', 'strong', 'self-assured', 'decisive', 'motivated', 'optimistic'
        ],
        'Emotional Intelligence': [
            'aware', 'emotions', 'regulate', 'empathy', 'understanding', 'composure', 'calm', 'patience', 'listening', 'self-control'
        ],
        'Leadership': [
            'leader', 'inspire', 'guide', 'vision', 'manage', 'responsibility', 'motivate', 'mentor', 'authority', 'decide'
        ],
        'Creativity': [
            'invent', 'design', 'innovate', 'imaginative', 'art', 'concept', 'original', 'idea', 'create', 'compose'
        ]
    }

    words = text.lower().split()
    if not words:
        return {trait: 0 for trait in trait_keywords}

    word_freq = collections.Counter(words)
    trait_scores = {trait: sum(word_freq[keyword] for keyword in keywords) for trait, keywords in trait_keywords.items()}

    total = sum(trait_scores.values())
    if total == 0:
        return {trait: 0 for trait in trait_keywords}

    return {trait: (score / total) * 100 for trait, score in trait_scores.items()}

class PersonalityPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Personality Predictor - Extended Version")
        self.root.geometry("650x750")
        self.root.configure(bg="#f0f0f0")

        tk.Label(root, text="AI Personality Predictor", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333").pack(pady=15)
        tk.Label(root, text="Enter text (100+ words recommended) to analyze your personality.", font=("Helvetica", 10), bg="#f0f0f0", fg="#555").pack(pady=(0, 10))

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, font=("Arial", 11), relief=tk.SOLID, borderwidth=1)
        self.text_area.pack(pady=10, padx=20)

        tk.Button(root, text="Analyze Personality", command=self.run_analysis, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief=tk.RAISED, borderwidth=2, padx=10, pady=5).pack(pady=10)

        results_frame = tk.Frame(root, bg="white", relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(results_frame, text="Results", font=("Helvetica", 14, "bold"), bg="white").pack(pady=10)
        self.results_text = tk.Label(results_frame, text="Your results will appear here.", justify=tk.LEFT, font=("Courier", 11), bg="white")
        self.results_text.pack(pady=5, padx=10, anchor="w")

    def run_analysis(self):
        user_text = self.text_area.get("1.0", tk.END).strip()
        if len(user_text) < 10:
            messagebox.showwarning("Input Error", "Please enter some text to analyze.")
            return
        self.display_results(analyze_text(user_text))

    def display_results(self, results):
        if not any(score > 0 for score in results.values()):
            self.results_text.config(text="Could not determine personality profile. Provide more detailed text.")
            return
        display = "".join(f"{trait:<25s} | {pct:5.1f}% | {'█' * int(pct / 2.5)}\n" for trait, pct in sorted(results.items(), key=lambda x: x[1], reverse=True))
        top_trait = max(results, key=results.get)
        summary = f"\nDominant Trait: {top_trait}\n(This result is a prototype prediction.)"
        self.results_text.config(text=display + summary + "\n\nExtended version.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityPredictorApp(root)
    root.mainloop()
