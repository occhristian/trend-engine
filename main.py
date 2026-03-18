from scraper import get_trends
# from analyzer import extract_keywords
from generator import generate_ideas


def main():
    print("[1/3] Fetching trends from X...")
    trends = get_trends()

    print("[2/3] Generating insights with AI...")
    ideas = generate_ideas(trends)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ideas)

    print("[3/3] Done. Check output.txt")

if __name__ == "__main__":
    main()