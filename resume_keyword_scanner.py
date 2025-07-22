import json
from collections import defaultdict
import matplotlib.pyplot as plt

# Load files
with open("resume_sample.txt", "r") as f:
    resume_text = f.read().lower()

with open("job_description_sample.txt", "r") as f:
    jd_text = f.read().lower()

with open("keywords.json", "r") as f:
    keyword_dict = json.load(f)

# Keyword match logic
match_summary = {}
missing_keywords = defaultdict(list)

for category, keywords in keyword_dict.items():
    total = len(keywords)
    matched = sum(1 for word in keywords if word.lower() in resume_text)
    match_summary[category] = {
        "matched": matched,
        "total": total,
        "missing": [word for word in keywords if word.lower() not in resume_text]
    }

# Print results
for category, data in match_summary.items():
    print(f"{category}: {data['matched']}/{data['total']} matched")
    if data['missing']:
        print("  Missing:", ", ".join(data['missing']))
    print()

# Bar chart
categories = list(match_summary.keys())
matched = [match_summary[cat]["matched"] for cat in categories]
total = [match_summary[cat]["total"] for cat in categories]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, total, color="#d9d9d9", label="Total")
ax.bar(categories, matched, color="#4caf50", label="Matched")
ax.set_title("Resume Keyword Match by Category")
ax.set_ylabel("Keyword Count")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("match_chart.png")
