import re


def evaluate_description(description):
    """
        Evaluates the credibility and specificity of a product description.

        Args:
            description (str): Product description to evaluate.

        Returns:
            dict: Score breakdown and final score.
        """
    score = 0
    breakdown = {
        "Specificity": 0,
        "Measurable Outcomes": 0,
        "Technical Transparency": 0,
        "Real-World Examples": 0,
        "Validation and Evidence": 0,
        "Red Flags Deduction": 0
    }

    # Specificity Check
    specificity_keywords = ["reduce", "optimize", "streamline", "enhance", "automate"]
    if any(keyword in description.lower() for keyword in specificity_keywords):
        breakdown["Specificity"] = 20

    # Measurable Outcomes Check
    if re.search(r"\d+%", description) or re.search(r"\$\d+", description) or re.search(r"\d+ (hours|days|weeks)",
                                                                                        description.lower()):
        breakdown["Measurable Outcomes"] = 25

    # Technical Transparency Check
    technical_keywords = ["GPT", "TensorFlow", "PyTorch", "machine learning", "deep learning", "neural network"]
    if any(keyword in description for keyword in technical_keywords):
        breakdown["Technical Transparency"] = 20

    # Real-World Examples Check
    example_phrases = ["used by", "partnered with", "adopted by", "implemented for"]
    if any(phrase in description.lower() for phrase in example_phrases):
        breakdown["Real-World Examples"] = 15

    # Validation and Evidence Check
    validation_phrases = ["recognized by", "certified", "awarded", "verified"]
    if any(phrase in description.lower() for phrase in validation_phrases):
        breakdown["Validation and Evidence"] = 10

    # Red Flags Deduction
    red_flag_keywords = ["cutting-edge", "revolutionary", "next-gen", "world-class", "state-of-the-art"]
    if any(keyword in description.lower() for keyword in red_flag_keywords):
        breakdown["Red Flags Deduction"] = -10

    # Calculate total score
    score = sum(breakdown.values())
    score = max(0, min(score, 100))  # Ensure score is between 0 and 100
    breakdown["Final Score"] = score

    return breakdown


# Example usage
description = "Our AI platform predicts inventory demand with 95% accuracy, reducing overstock costs by 20% annually."
print(f"Score: {evaluate_description(description)}")
description = "Using GPT-4 and custom neural networks, we improved customer support response time by 40% for over 500 clients."
print(f"Score: {evaluate_description(description)}")
description = "Our solution automates invoice processing, saving companies an average of 2,000 hours per year and reducing errors by 30%."
print(f"Score: {evaluate_description(description)}")
description = "Integrated with TensorFlow, our image recognition tool identifies defects in manufacturing lines with 98% precision, reducing downtime by 15%."
print(f"Score: {evaluate_description(description)}")
description = "Our fraud detection model, trained on real-world banking data, cut fraudulent transactions by 50% within six months for BankCorp."
print(f"Score: {evaluate_description(description)}")

description = "Our AI helps e-commerce businesses optimize pricing strategies and increase revenue."
print(f"Score: {evaluate_description(description)}")
description = "Using advanced machine learning algorithms, our system improves supply chain efficiency for mid-sized enterprises."
print(f"Score: {evaluate_description(description)}")
description = "We leverage natural language processing to enhance customer experience in call centers worldwide."
print(f"Score: {evaluate_description(description)}")
description = "Our product streamlines document processing, making workflows more efficient for over 100 clients."
print(f"Score: {evaluate_description(description)}")
description = "Built on PyTorch, our recommendation engine boosts user engagement on digital platforms."
print(f"Score: {evaluate_description(description)}")

description = "Our cutting-edge AI transforms business operations and drives growth in multiple industries."
print(f"Score: {evaluate_description(description)}")
description = "With state-of-the-art machine learning, our platform is revolutionizing retail analytics."
print(f"Score: {evaluate_description(description)}")
description = "Our solution enhances productivity and reduces costs using advanced AI techniques."
print(f"Score: {evaluate_description(description)}")
description = "Harnessing the power of deep learning, our product delivers unparalleled insights."
print(f"Score: {evaluate_description(description)}")
description = "We deploy AI to improve efficiency across all departments in your organization."
print(f"Score: {evaluate_description(description)}")

description = "Our AI is the most advanced on the market, making everything easier."
print(f"Score: {evaluate_description(description)}")
description = "This revolutionary technology is changing the world as we know it."
print(f"Score: {evaluate_description(description)}")
description = "Our platform guarantees better results and smarter decisions for your business."
print(f"Score: {evaluate_description(description)}")
description = "Powered by proprietary AI, our solution ensures you stay ahead of competitors."
print(f"Score: {evaluate_description(description)}")
description = "Experience unparalleled innovation with our AI-driven, next-gen platform."
print(f"Score: {evaluate_description(description)}")

