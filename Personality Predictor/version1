import tkinter as tk
from tkinter import scrolledtext, messagebox
import collections

def analyze_text(text):
    """
    Analyzes the input text to predict personality traits based on the Big Five model.
    This core logic remains the same as the previous version.
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
            'party', 'people', 'social', 'talkative', 'team', 'together'
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
        ]
    }
    
    words = text.lower().split()
    word_count = len(words)

    if word_count == 0:
        return {trait: 0 for trait in trait_keywords}

    word_freq = collections.Counter(words)
    
    trait_scores = {trait: sum(word_freq[keyword] for keyword in keywords) for trait, keywords in trait_keywords.items()}

    total_trait_words = sum(trait_scores.values())
    if total_trait_words == 0:
        return {trait: 0 for trait in trait_keywords}

    return {trait: (score / total_trait_words) * 100 for trait, score in trait_scores.items()}


class PersonalityPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Personality Predictor")
        self.root.geometry("600x650")
        self.root.configure(bg="#f0f0f0")

        # --- UI Elements ---
        
        # Title Label
        title_label = tk.Label(root, text="AI Personality Predictor", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=15)
        
        # Instructions
        instructions_label = tk.Label(
            root, 
            text="Enter a block of text (at least 100 words for best results)\nto analyze your personality based on the Big Five model.",
            font=("Helvetica", 10), 
            bg="#f0f0f0", 
            fg="#555"
        )
        instructions_label.pack(pady=(0, 10))
        
        # Text Input Area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, font=("Arial", 11), relief=tk.SOLID, borderwidth=1)
        self.text_area.pack(pady=10, padx=20)
        
        # Analyze Button
        analyze_button = tk.Button(root, text="Analyze Personality", command=self.run_analysis, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief=tk.RAISED, borderwidth=2, padx=10, pady=5)
        analyze_button.pack(pady=10)
        
        # Results Frame
        results_frame = tk.Frame(root, bg="#ffffff", relief=tk.SOLID, borderwidth=1)
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        results_title = tk.Label(results_frame, text="Results", font=("Helvetica", 14, "bold"), bg="white")
        results_title.pack(pady=10)

        self.results_text = tk.Label(results_frame, text="Your results will appear here.", justify=tk.LEFT, font=("Courier", 11), bg="white")
        self.results_text.pack(pady=5, padx=10, anchor="w")

    def run_analysis(self):
        user_text = self.text_area.get("1.0", tk.END)
        if len(user_text.strip()) < 10:
            messagebox.showwarning("Input Error", "Please enter some text to analyze.")
            return

        results = analyze_text(user_text)
        self.display_results(results)

    def display_results(self, results):
        if not any(score > 0 for score in results.values()):
            self.results_text.config(text="Could not determine a personality profile.\nTry providing a longer and more descriptive text.")
            return

        sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
        
        display_text = ""
        for trait, percentage in sorted_results:
            bar = '█' * int(percentage / 2.5) # Scale bar for GUI
            display_text += f"{trait:<20s} | {percentage:5.1f}% | {bar}\n"
        
        display_text += "\nprototype version, not completed yet."
        
        self.results_text.config(text=display_text)


if __name__ == "__main__":
    # Create the main window and run the application
    main_window = tk.Tk()
    app = PersonalityPredictorApp(main_window)
    main_window.mainloop()

