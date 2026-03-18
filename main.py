from scraper import get_trends
from analyzer import extract_keywords
from generator import generate_ideas

def main():
    print("Fetching trends...")
    trends = get_trends()

    print("Analyzing trends...")
    keywords = extract_keywords(trends)

    print("Generating ideas...")
    ideas = generate_ideas(keywords)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ideas)

    print("Done. Check output.txt")

if __name__ == "__main__":
    main()