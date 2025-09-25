# SQL-and-Python-Music-Analytics-Decision-Making

This project was developed to combine **Python** and **SQL** for extracting, organizing, and analyzing real-world music data.

---

## 📌 Objectives

- Consolidate Python and SQL knowledge in a real-world project.  
- Automate data extraction from music APIs (Spotify and Last.fm).  
- Design and populate a relational database using SQL.  
- Perform analysis through SQL queries to answer business-driven questions.  
- Apply Agile principles with iterative sprints, including **daily stand-ups**, **sprint reviews**, and **retrospectives** to maintain alignment, inspect progress, and continuously improve.

---

## 🔄 Project Phases

### Phase 1: Data Extraction
- Used the **Spotify Web API** to retrieve information about tracks, albums, artists, and release years.  
- Focused on the period **2016–2020** across selected genres (e.g., Rock, Pop, Jazz).  
- Enriched dataset with **Last.fm API** to capture popularity and play statistics.  

**Example — Python function to extract tracks by genre and year:**

```python
def call(genre):
    results = []
    artist_list = []
    for year in range(2016, 2021):
        for offset in range(0, 500, 50):
            datos = sp.search(
                q=f'genre:{genre}, year:{year}',
                type='track',
                limit=50,
                offset=offset)
            for item in datos['tracks']['items']:
                release_date = item['album']['release_date']
                if release_date.startswith(str(year)):
                    info = {   
                        'nombre_artista': item['artists'][0]['name'],
                        'album': item['album']['name'],
                        'fecha': item['album']['release_date'],
                        'tipo': item['type'],
                        'track': item['name']}
                    results.append(info)
    return results
```

---

### Phase 2: Automation with `src/`
To make the workflow scalable and maintainable, I created the `src/` folder to organize reusable Python scripts:

- `support_call_api.py` → Functions to handle Spotify API calls.  
- `data_manipulation.py` → Functions to process and export data.  

**Example — Export function:**

```python
def extract_artist(results, genre):
    df = pd.DataFrame(results)
    fileName = f'track_{genre}.csv'
    df.to_csv(fileName, index=False)
```

**Example — Automated loop for multiple genres:**

```python
from src import support_call_API as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz', 'pop', 'classical']
for genre in genre_list:
    resultados, artist_list = ap.call(genre)
    dm.extract_artist(resultados, genre)
```

This approach allows adding new genres simply by updating the list — keeping the pipeline reproducible and easy to maintain.

---

### Phase 3: Database Design and Storage
- Designed a relational schema in **MySQL** to store the extracted data.  
- Created tables for **artists, tracks, albums, genres, and popularity metrics**.  
- Inserted and validated data while ensuring referential integrity and avoiding duplicates.  

**Example — Environment setup for API authentication:**

```python
env_path = 'api.env' 
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("CLIENT_ID or CLIENT_SECRET not found in environment variables.")
```

**Example — SQL schema & updates:**

```sql
CREATE TABLE Tabla_artist (
    id_artist INT AUTO_INCREMENT PRIMARY KEY,
    id_gender INT,
    artist_name VARCHAR(50) NOT NULL,
    album VARCHAR(100) NOT NULL,
    date DATE,
    type VARCHAR(10) NOT NULL,
    track VARCHAR(100) NOT NULL,
    CONSTRAINT fk_id_gender FOREIGN KEY (id_gender)
        REFERENCES Table_gender(id_gender)
);

UPDATE tabla_artista a
JOIN tabla_tracks t ON a.id_artist = t.id_artista
SET a.album = t.album;

ALTER TABLE table_biography MODIFY COLUMN bio LONGTEXT;

UPDATE table_biography
SET artist = REPLACE(REPLACE(REPLACE(artista, '[', ''), ']', ''), '''', '');
```

---

### Phase 4: Analysis and Decision-Making
Key business questions explored with SQL queries:

- Which artist released the most albums?  
- Which genre shows the highest popularity?  
- In which year were the most albums released?  
- Which track is the top-ranked by popularity?  
- Which artist accumulates the highest overall rating?  
- Which countries or regions show the highest concentration of listener activity (using regional endpoints or metadata)?

These queries allowed to uncover patterns in artist collaborations, popularity trends, and geographical listener preferences whenever regional data was available.

---

## 🌍 International vs Local Data

- **Spotify API**: The `/search` endpoint queries the **global catalog** unless a `market` parameter is specified. Without it, results are international by default.  
- **Last.fm API**: Returns global data by default, but offers endpoints (e.g., `geo.getTopArtists`) to filter by country or region if needed.  

---

## 📂 Repository Structure

```
SQL-AND-PYTHON-MUSIC-ANALYTICS-DECISION-MAKING/
│
├── Jupyter Notebooks/
│   ├── .cache/
│   ├── API_album.ipynb
│   ├── bio.ipynb
│   └── stats.ipynb
│
├── Python+SQL/
│   ├── CSV_to_SQL.ipynb
│   ├── mysql.connector.ipynb
│   └── mysqlconnector_to_csv.ipynb
│
├── SQL/
│   ├── bddd-from-scratch.sql
│   └── reasearch-questions-final-queries.sql
│
├── src/
│   ├── __pycache__/
│   ├── data_manipulation.py
│   └── support_call_api.py
│
├── .cache/
├── .gitignore
├── api.env
├── main.py
├── README.md
│
├── track_jazz.csv
├── track_pop.csv
└── track_rock.csv
```

---

## 📅 Agile Workflow

- Work planned in **2-week sprints** with backlog tracking, **daily stand-ups**, **sprint reviews**, and **retrospectives**.  
- Early progress was documented collaboratively → later iterations were continued independently.  
- Challenges and learnings were continuously documented to improve ways of working.

---

## ✅ Key Deliverables

- Automated Python scripts for data extraction and transformation.  
- SQL schema and database population scripts.  
- Analytical SQL queries that not only answer music industry questions (e.g., releases, popularity, collaborations) but also generate actionable insights to support **product strategy**, **marketing decisions**, and **content planning**.  
- Clear documentation and organized repository for reproducibility.

---

## 📊 Final Presentation

The project concludes with a presentation that covers:  
- Objectives and methodology.  
- Python automation and SQL analytics.  
- Key findings and insights to support decision-making.  
- Lessons learned and improvements for future iterations.

---

## 👩‍💻 Author & Role

The work started in a **cross-functional team environment**, where I led scope alignment and the initial API strategy. We practiced shared code ownership and pair programming to accelerate delivery and ensure high-quality results.  
We held **daily stand-ups** for alignment and progress tracking, as well as **sprint reviews** and **retrospectives** to adapt and improve.  

I’ve been iterating on the project independently to raise its quality bar: refactoring code for clarity and reliability, removing sources of error, and automating repeatable tasks (starting with CSV exports via `support_call_api.py` and `data_manipulation.py`). I also created and refined the SQL schema and developed the queries that generate decision-ready insights. Throughout, I balanced hands-on coding with leadership—aligning stakeholders, managing delivery risks, and keeping documentation crisp—so the work remains transparent, scalable, and impactful.

---

## 🚀 Next Steps

Currently expanding the project by **automating artist biographies, statistics ingestion** and **SQL** — applying the same ETL approach used for the main datasets to enrich the database further.
