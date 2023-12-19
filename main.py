import requests
import csv
import tkinter as tk
from tkinter import font

def fetch_quote(root):
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        author = data["author"]
        quote = data["content"]
        tags = ", ".join(data["tags"])

        print(f"Author: {author}")
        print(f"Quote: {quote}")
        print(f"Tags: {tags}")

        # Use a different font and color for the quote
        quote_font = font.Font(size=14, weight='bold', slant='italic')
        quote_label.config(text=f'"{quote}"\n\n- {author}\n\nTags: {tags}', font=quote_font, fg='blue')

        # Set the new command for both buttons
        tick_button.config(command=lambda: save_to_csv('favorites.csv', author, quote, tags, root))
        cross_button.config(command=lambda: save_to_csv('rejected.csv', author, quote, tags, root))

    else:
        print(f"Failed to fetch quote. Status code: {response.status_code}")

def save_to_csv(file_path, author, quote, tags, root):
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([author, quote, tags])
    
    print(f"Quote saved to {file_path}")

    # Fetch a new quote after saving to CSV
    fetch_quote(root)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quote App")

    # Create initial UI
    quote_label = tk.Label(root, text="", font=font.Font(size=14), fg='blue')
    quote_label.pack(pady=10)

    tick_button = tk.Button(root, text="✔ Add to Favorites", command=lambda: None, fg='green')  # Placeholder command
    tick_button.pack(side=tk.LEFT, padx=10)

    cross_button = tk.Button(root, text="✘ Add to Rejected", command=lambda: None, fg='red')  # Placeholder command
    cross_button.pack(side=tk.RIGHT, padx=10)

    # Fetch the first quote
    fetch_quote(root)

    root.mainloop()
