# 🎬 Top 100 Movies Scraper

A Python web scraper that pulls Empire magazine's **100 Greatest Movies** list straight from a web page, extracts every title with `BeautifulSoup`, flips the list into proper rank order, and saves it to a clean text file — a ready-made "must-watch" checklist generated in under a second.

> Point it at a page, and it turns messy HTML into a tidy, ranked movie list you can actually use.

---

## 🎮 Demo

Running `python main.py` produces a `movies.txt` file ranked from #1 to #100:

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
5) Pulp Fiction
...
98) Amelie
99) Raging Bull
100) Stand By Me
```

<!-- Optional: add a screenshot of the terminal run or the generated movies.txt here -->

---

## ✨ Features

- 🌐 **Live page fetching** with `requests`, with explicit UTF-8 decoding so special characters (like the accent in *Léon*) come through correctly.
- 🛡️ **Fail-loud error handling** — `raise_for_status()` stops the script immediately if the download fails, instead of silently writing an empty file.
- 🕰️ **Archived source for stability** — scrapes a Wayback Machine snapshot of the original article, so the scraper keeps working even if the live page changes or disappears.
- 🔍 **Targeted HTML parsing** using `BeautifulSoup` to locate each movie title by its tag and CSS class (`h3.title`).
- 🔄 **Automatic rank reordering** — the page lists entries counting down from 100, so the script reverses them to produce a #1 → #100 list.
- 💾 **Clean file output** — one title per line, saved to `movies.txt`, ready to use as a watchlist or feed into another project.

---

## 🛠️ Tech Stack

| Category | Tool / Concept |
|---|---|
| Language | Python 3 |
| HTTP Requests | `requests` |
| HTML Parsing | `beautifulsoup4` (`html.parser`) |
| Data Source | [Wayback Machine](https://web.archive.org/) snapshot of Empire's "100 Greatest Movies" article |
| Core Concepts | Web scraping, DOM navigation, CSS class selection, list comprehensions, file I/O |

---

## 📂 Project Structure

```
Movie Scraper/
│
├── main.py       # Scraper — fetches, parses, reorders, and saves the list
├── movies.txt     # Generated output — the ranked movie list
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- `requests` and `beautifulsoup4` — install via pip:

```bash
pip install requests beautifulsoup4
```

### Run it
```bash
git clone https://github.com/VISHAL108-Mech/Python-Movie-Ranking-Scraper.git
cd movie-scraper
python main.py
```

A fresh `movies.txt` appears in the project folder with all 100 titles.

---

## 🧩 How It Works

### 1. Fetching the Page
The script requests an archived copy of the article, checks that the request succeeded with `raise_for_status()`, and forces UTF-8 decoding so accented characters and special punctuation in movie titles aren't garbled.

```python
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(url=URL)
r.raise_for_status()
r.encoding = "utf-8"
data = r.text
```

### 2. Parsing the HTML
`BeautifulSoup` turns the raw HTML into a searchable tree. Inspecting the page showed that every movie title sits inside an `<h3 class="title">` tag, so `find_all()` collects them all in one call.

```python
soup = BeautifulSoup(data, "html.parser")
all_movies_name = soup.find_all(name="h3", class_="title")
```

### 3. Extracting the Titles
A list comprehension pulls the visible text out of each tag, discarding the HTML around it.

```python
movies_list = [movie.getText() for movie in all_movies_name]
```

### 4. Reordering & Saving
The page counts down from 100 to 1, so the list is reversed to put the #1 film first, then written out one title per line.

```python
with open("movies.txt", "w") as file:
    for movie in reversed(movies_list):
        file.write(f"{movie}\n")
```

---

## 📚 What This Project Demonstrates

- The core web-scraping workflow: **request → parse → extract → store**
- Reading a page's HTML structure to find the right tag and class to target
- Handling text encoding correctly when scraping international titles
- Validating HTTP responses so failures surface immediately instead of producing bad output
- Choosing a stable data source (an archived snapshot) instead of depending on a live page
- Transforming scraped data (reversing order) before saving it

---

## ⚖️ Responsible Scraping

This project is for learning and personal use. It reads a publicly archived page once per run and makes a single request. If you adapt it to other sites, check their `robots.txt` and terms of service, and avoid sending rapid repeated requests.

---

## 🔮 Future Improvements

- [ ] Number the titles in code with `enumerate()` instead of relying on the numbering embedded in the page's text, which would also normalize inconsistent source formatting (a couple of entries on the original page use `:` instead of `)` or carry the wrong number)
- [ ] Export to CSV or JSON, with separate rank and title fields
- [ ] Add a command-line argument for the URL so the scraper works on other "top 100" list pages
- [ ] Enrich each movie with details (year, director, rating) from a movie API

---

## 👤 Developer

**VISHAL YADAV**
- GitHub: [@VISHAL108-Mech](https://github.com/VISHAL108-Mech)
- LinkedIn: [vishal-yadav-2a91a7428](https://www.linkedin.com/in/vishal-yadav-2a91a7428)
- Email: [vy4122000@gmail.com](mailto:vy4122000@gmail.com)
