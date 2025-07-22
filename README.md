# Resume Keyword Scanner

A Python project that checks how well a resume matches a job description using keyword categories like **Tools**, **Skills**, **Soft Skills**, **Certifications**, and **Job Terms**. It generates both a match report and a visual chart to help improve your resume alignment with job posts.

---

## Included Files

* `resume_keyword_scanner.py` – main script
* `resume_keyword_scanner.ipynb` – Jupyter Notebook version
* `resume_sample.txt` – sample resume
* `job_description_sample.txt` – sample job description
* `keywords.json` – editable list of keyword categories
* `match_report.txt` – generated match summary
* `match_chart.png` – chart showing match percentages

---

## How to Use

1. Make sure you have Python 3 installed
2. Put the following files in the same directory:

   * `resume_sample.txt`
   * `job_description_sample.txt`
   * `keywords.json`
3. Run the script:

   ```
   python resume_keyword_scanner.py
   ```

   or open the Jupyter notebook:

   ```
   jupyter notebook resume_keyword_scanner.ipynb
   ```
4. The script will generate:

   * `match_report.txt`
   * `match_chart.png`

---

## Customize Keywords

You can edit `keywords.json` to adjust which keywords to look for in each category:

```json
{
  "Tools": ["Excel", "SQL", "Power BI", "Tableau"],
  "Skills": ["Data Cleaning", "Dashboarding", "Reporting"],
  "Soft Skills": ["Communication", "Leadership"],
  "Certifications": ["Google Analytics"],
  "Job Terms": ["Data Analyst"]
}
```

---

## Example Output

```
Tools — 5/6 matched
  Missing: Tableau

Skills — 4/5 matched
  Missing: Data Cleaning

Soft Skills — 0/4 matched
  Missing: Communication, Collaboration, Problem Solving, Leadership

Certifications — 0/3 matched
  Missing: Certified Data Analyst, Google Analytics, AWS Data Analytics

Job Terms — 0/3 matched
  Missing: Data Analyst, Reporting Analyst, Business Intelligence
```

---

## Requirements

* Python 3.x
* matplotlib

To install matplotlib, run:

```
pip install matplotlib
```

---

## License

Free to use, modify, and share.


