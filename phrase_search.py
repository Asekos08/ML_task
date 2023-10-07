from keyphrase_vectorizers import KeyphraseCountVectorizer
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = KeyphraseCountVectorizer()

standard_phrases = [
    "Optimal performance",
    "Utilise resources",
    "Enhance productivity",
    "Conduct an analysis",
    "Maintain a high standard",
    "Implement best practices",
    "Ensure compliance",
    "Streamline operations",
    "Foster innovation",
    "Drive growth",
    "Leverage synergies",
    "Demonstrate leadership",
    "Exercise due diligenc",
    "Maximize stakeholder value",
    "Prioritise tasks",
    "Facilitate collaboration",
    "Monitor performance metric",
    "Execute strategies",
    "Gauge effectiveness",
    "Champion change"
]

def phrase_seeker(input_text):
    vectorizer.fit_transform(input_text).toarray()
    keyphrases = list(vectorizer.get_feature_names_out())
    return keyphrases


class TextAnalyzer:
    def __init__(self, standard_phrases):
        self.nlp = spacy.load("en_core_web_sm")
        self.standard_phrases = standard_phrases

    def get_phrase_vector(self, phrase):
        tokens = self.nlp(phrase)
        vector = np.mean([token.vector for token in tokens], axis=0)
        return vector

    def analyze_text(self, input_text):
        input_vector = [self.get_phrase_vector(phrase) for phrase in input_text]

        similarity_scores = cosine_similarity(input_vector, [self.get_phrase_vector(phrase) for phrase in self.standard_phrases])

        suggestions = []
        for i in range (len(similarity_scores)):
            for j, score in enumerate(similarity_scores[i]): 
                if score > 0.75:  
                    suggestions.append({
                        "original": input_text[i],
                        "replacement": self.standard_phrases[j],
                        "similarity_score": score
                    })

        return suggestions

def reccomend_option():
    input_text = input("Enter your text: ").split('.')
    input_text.remove('')
    input_phrases = phrase_seeker(input_text)
    

    analyzer = TextAnalyzer(standard_phrases)
    suggestions = analyzer.analyze_text(input_phrases)

    print("Suggestions: ")
    for suggestion in suggestions:
        print(f"Original: {suggestion['original']}")
        print(f"Replacement: {suggestion['replacement']}")
        print(f"Similarity Score: {suggestion['similarity_score']}\n")

reccomend_option()

