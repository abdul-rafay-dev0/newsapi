import requests

API_KEY = open("api_key.txt").read().strip()
URL = "https://newsapi.org/v2/everything"


def fetch_news(topic):
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()

        news_data = response.json()
        articles = news_data.get("articles", [])

        print(f"\n--- Found {len(articles)} articles on '{topic}' ---\n")
        for index, article in enumerate(articles, start=1):
            print(f"{index}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Author: {article['author']}")
            print(f"   URL: {article['url']}\n")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error occurred: {err}")
        print(response.json().get("message", "No error message provided."))
    except Exception as err:
        print(f"An error occurred: {err}")


while True:
    print("=========================================")
    print("GLOBAL NEWS DASHBOARD (LIVE)")
    print("=========================================")
    print("1. Weather & Climate News")
    print("2. Sports & Racing Updates")
    print("3. Technology & Space News")
    print("4. Business & Market Data")
    print("5. Exit Program")
    print("=========================================")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        fetch_news("climate")
    elif choice == "2":
        fetch_news("racing")
    elif choice == "3":
        fetch_news("technology")
    elif choice == "4":
        fetch_news("business")
    elif choice == "5":
        print("Closing the news terminal. Goodbye!")
        break
    else:
        print("Invalid selection! Please enter a number from 1 to 5.")

    input("Press Enter to return to the main menu...")
    print("\n" * 2)