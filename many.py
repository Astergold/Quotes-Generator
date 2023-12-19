import requests
import csv

def fetch_quotes(num_quotes=5000):
    url = "https://api.quotable.io/random"
    
    with open('quotes2.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        for _ in range(num_quotes):
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                author = data["author"]
                quote = data["content"]
                tags = ", ".join(data["tags"])

                print(f"Author: {author}")
                print(f"Quote: {quote}")
                print(f"Tags: {tags}")

                # Write data to a CSV file
                writer.writerow([author, quote, tags])

            else:
                print(f"Failed to fetch quote. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_quotes(5000)
