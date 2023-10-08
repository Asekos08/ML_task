# Keyphrase Substitution Recommender

## Overview

This project aims to recommend substitutions for phrases in a given text based on the similarity to a list of standard phrases. The key components of the project include a custom `KeyphraseCountVectorizer` for extracting keyphrases, a `TextAnalyzer` class for computing similarity scores, and a recommendation function (`recommend_option`) for user interaction.

## Dependencies

- `keyphrase_vectorizers`: A custom module for implementing the `KeyphraseCountVectorizer`.
- `spacy`: A natural language processing library for tokenization and vectorization.
- `numpy`: A library for numerical operations, used for calculating vector means.
- `sklearn`: A machine learning library, used for cosine similarity computation.

Install dependencies using:

```bash
pip install keyphrase_vectorizers spacy numpy scikit-learn
```

Download the SpaCy English model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

### Keyphrase Extraction:

- The phrase_seeker function takes input text, utilizes KeyphraseCountVectorizer to extract keyphrases, and returns a list of keyphrases.
  
### Text Analysis and Recommendations:

- The TextAnalyzer class is responsible for analyzing the input text and recommending substitutions.
- Instantiate TextAnalyzer with a list of standard phrases.
- Use the analyze_text method to compute similarity scores and generate substitution suggestions.

## User Interaction:

- The recommend_option function serves as a user interface for receiving input text and displaying substitution recommendations.
- Run the function to enter your text, and the system will suggest replacements based on similarity scores.
  
Customization
Adjust the standard_phrases list to include phrases relevant to your domain.
Tune the similarity threshold in the analyze_text method for more precise recommendations.
Feel free to enhance the keyphrase extraction or similarity computation methods based on your specific requirements.

### Run the recommendation function
- recommend_option()
