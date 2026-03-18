def generate_ideas(keywords):
    ideas = ""

    for keyword in keywords[:5]:
        ideas += f"\n🔥 Trend Focus: {keyword.capitalize()}\n"

        ideas += "Product Ideas:\n"
        ideas += f"- 14-day {keyword} challenge (subscription)\n"
        ideas += f"- Personalized {keyword} plan generator\n"

        ideas += "Content Hooks:\n"
        ideas += f"- 'Why your {keyword} strategy isn’t working'\n"
        ideas += f"- 'The fastest way to improve {keyword}'\n"

        ideas += "Monetization:\n"
        ideas += "- Subscription model ($9.99/month)\n"
        ideas += "- Free trial → paid conversion funnel\n"

    return ideas