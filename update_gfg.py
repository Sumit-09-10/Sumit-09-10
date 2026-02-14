import requests
from bs4 import BeautifulSoup
import re

# ==============================
# CONFIGURATION
# ==============================
GFG_USERNAME = "Sumit-09-10"
README_FILE = "README.md"

# ==============================
# FETCH GFG DATA
# ==============================

url = f"https://auth.geeksforgeeks.org/user/{GFG_USERNAME}/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Try to locate score & rank
score = "Not Found"
rank = "Not Found"

try:
    score_section = soup.find(text=re.compile("Coding Score"))
    if score_section:
        score = score_section.find_next().text.strip()
except:
    pass

try:
    rank_section = soup.find(text=re.compile("Institute Rank"))
    if rank_section:
        rank = rank_section.find_next().text.strip()
except:
    pass

print("Score:", score)
print("Rank:", rank)

# ==============================
# UPDATE README
# ==============================

with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r"(<!-- GFG_SCORE_START -->)(.*?)(<!-- GFG_SCORE_END -->)",
    rf"\1{score}\3",
    content,
    flags=re.DOTALL,
)

content = re.sub(
    r"(<!-- GFG_RANK_START -->)(.*?)(<!-- GFG_RANK_END -->)",
    rf"\1{rank}\3",
    content,
    flags=re.DOTALL,
)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated successfully.")
