import pandas as pd
import spacy
from collections import Counter
import re

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Keywords for product descriptions
VAGUE_KEYWORDS = {"solution", "innovative", "advanced", "revolutionary", "leading"}
DETAILED_KEYWORDS = {"optimize", "reduce", "increase", "automate", "integrate"}

def analyze_product_description(description):
    """
    Analyze a product description for specificity and technical details.
    """
    doc = nlp(description)
    word_count = sum(1 for token in doc if not token.is_punct)  # Exclude punctuation
    entity_counts = Counter(ent.label_ for ent in doc.ents)  # Count entity types

    # Entity density: total entities per word
    total_entities = sum(entity_counts.values())
    entities_per_word = total_entities / word_count if word_count > 0 else 0

    # Presence of numbers
    has_numbers = bool(re.search(r'\d+[%$]', description))

    # Keyword Scoring
    word_counts = Counter(token.text.lower() for token in doc)
    vague_keywords_count = sum(word_counts[word] for word in VAGUE_KEYWORDS if word in word_counts)
    detailed_keywords_count = sum(word_counts[word] for word in DETAILED_KEYWORDS if word in word_counts)

    # Check for technical terms
    technical_terms = {"AI", "GPT", "TensorFlow", "PyTorch"}
    has_technical_terms = any(term in description for term in technical_terms)

    return {
        'description': description,
        'word_count': word_count,
        'total_entities': total_entities,
        'entities_per_word': entities_per_word,
        'has_numbers': has_numbers,
        'vague_keywords_count': vague_keywords_count,
        'detailed_keywords_count': detailed_keywords_count,
        'has_technical_terms': has_technical_terms
    }

def grade_description(features):
    """
    Grade a product description based on analyzed features for specificity.
    Normalize to the range 0 to 1.
    """
    score = 0

    # Feature Scoring
    score += features['entities_per_word'] * 0.3
    if features['has_numbers']:
        score += 0.25
    if features['has_technical_terms']:
        score += 0.2
    detailed_keywords_score = features['detailed_keywords_count'] / max(1, features['word_count'])
    score += detailed_keywords_score * 0.25
    vague_keywords_score = features['vague_keywords_count'] / max(1, features['word_count'])
    score -= vague_keywords_score * 0.2

    # Normalize score
    score = max(0, min(1, score))
    return score

# Example usage
descriptions = [
    "Our AI reduces overstock by 15% using GPT-4 technology.",
    "This solution is innovative and revolutionizes business workflows.",
    "Integrated with TensorFlow, it optimizes operations and reduces costs by 20%.",
    "Our product helps companies automate processes with advanced AI.",
    "Increase productivity by 30% with our machine learning platform."
    "Our AI-driven chatbot decreased customer wait times by 50%, improving satisfaction ratings by 30%.",
    "Using machine learning, we automated invoice processing, saving businesses an average of $500,000 annually.",
    "Our supply chain AI reduced inventory waste by 20% in its first year for RetailCo.",
    "Leveraging deep learning, our tool detects manufacturing defects with 98.5% precision, reducing downtime by 25%.",
    "Certified by ISO, our AI forecasts energy usage, cutting costs by 15% for major utilities.",
    "Our platform optimizes marketing campaigns, improving engagement for digital advertisers.",
    "Built on TensorFlow, our AI enhances customer support workflows for call centers.",
    "We use advanced machine learning to analyze sales data and provide actionable insig,hts.",
    "Our product integrates neural networks to improve productivity across various sectors.",
    "AI-driven solutions from our company streamline HR processes for mid-sized firms.",
    "Our revolutionary AI transforms businesses by unlocking hidden efficiencies.",
    "Using state-of-the-art algorithms, we enhance decision-making across industries.",
    "Our AI automates workflows to save time and money for enterprises.",
    "We bring cutting-edge solutions to businesses looking to adopt AI.",
    "Our platform leverages world-class AI for next-generation insights.",
    "Our product uses AI magic to solve all your business problems.",
    "This groundbreaking technology redefines what’s possible with artificial intelligence.",
    "Our next-gen platform guarantees better results, faster.",
    "AI is at the core of our solution, delivering world-class results.",
    "We provide unmatched innovation through our proprietary AI-driven platform."
]

data = []
for desc in descriptions:
    features = analyze_product_description(desc)
    specificity_score = grade_description(features)
    features['specificity_score'] = specificity_score
    data.append(features)

# Convert data to DataFrame and display
df = pd.DataFrame(data)
print(df)



# Example usage
# description = "Our AI platform predicts inventory demand with 95% accuracy, reducing overstock costs by 20% annually."
# print(f"Score: {evaluate_description(description)}")
# description = "Using GPT-4 and custom neural networks, we improved customer support response time by 40% for over 500 clients."
# print(f"Score: {evaluate_description(description)}")
# description = "Our solution automates invoice processing, saving companies an average of 2,000 hours per year and reducing errors by 30%."
# print(f"Score: {evaluate_description(description)}")
# description = "Integrated with TensorFlow, our image recognition tool identifies defects in manufacturing lines with 98% precision, reducing downtime by 15%."
# print(f"Score: {evaluate_description(description)}")
# description = "Our fraud detection model, trained on real-world banking data, cut fraudulent transactions by 50% within six months for BankCorp."
# print(f"Score: {evaluate_description(description)}")
#
# description = "Our AI helps e-commerce businesses optimize pricing strategies and increase revenue."
# print(f"Score: {evaluate_description(description)}")
# description = "Using advanced machine learning algorithms, our system improves supply chain efficiency for mid-sized enterprises."
# print(f"Score: {evaluate_description(description)}")
# description = "We leverage natural language processing to enhance customer experience in call centers worldwide."
# print(f"Score: {evaluate_description(description)}")
# description = "Our product streamlines document processing, making workflows more efficient for over 100 clients."
# print(f"Score: {evaluate_description(description)}")
# description = "Built on PyTorch, our recommendation engine boosts user engagement on digital platforms."
# print(f"Score: {evaluate_description(description)}")
#
# description = "Our cutting-edge AI transforms business operations and drives growth in multiple industries."
# print(f"Score: {evaluate_description(description)}")
# description = "With state-of-the-art machine learning, our platform is revolutionizing retail analytics."
# print(f"Score: {evaluate_description(description)}")
# description = "Our solution enhances productivity and reduces costs using advanced AI techniques."
# print(f"Score: {evaluate_description(description)}")
# description = "Harnessing the power of deep learning, our product delivers unparalleled insights."
# print(f"Score: {evaluate_description(description)}")
# description = "We deploy AI to improve efficiency across all departments in your organization."
# print(f"Score: {evaluate_description(description)}")
#
# description = "Our AI is the most advanced on the market, making everything easier."
# print(f"Score: {evaluate_description(description)}")
# description = "This revolutionary technology is changing the world as we know it."
# print(f"Score: {evaluate_description(description)}")
# description = "Our platform guarantees better results and smarter decisions for your business."
# print(f"Score: {evaluate_description(description)}")
# description = "Powered by proprietary AI, our solution ensures you stay ahead of competitors."
# print(f"Score: {evaluate_description(description)}")
# description = "Experience unparalleled innovation with our AI-driven, next-gen platform."
# print(f"Score: {evaluate_description(description)}")
#
