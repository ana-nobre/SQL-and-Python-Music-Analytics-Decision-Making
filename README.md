# SQL-and-Python-Music-Analytics-Decision-Making

This project integrates **Python** and **SQL** to extract and transform music data from **APIs**, **export it to CSV files**, and **build a SQL database from scratch**. It concludes with **analytical SQL queries** that generate insights to support **data-driven decision-making** in the music industry.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-green)


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
def get_album(genre, start_year=2020, end_year=2025):
    resultados_album = []

    for offset in range(0, 500, 50):  # start stop step 
        datos = sp.search(q=f'{genre}', type='album', limit=50, offset=offset)

        for album in datos['albums']['items']:
            release_date = album.get('release_date', '')
            for year in range(start_year,end_year): 
                if release_date.startswith(str(year)):
                    info = {
                        'album': album['name'],
                        'fecha': release_date,
                        'tipo': album['album_type'],
                        'id': album['id']  
                    }
                    print("El nombre del álbum es:", info['album'])
                    print("La fecha de lanzamiento es:", info['fecha'])
                    print("Tipo:", info['tipo'])
                    print("..........")
                    
                    resultados_album.append(info)
                    break

    return resultados_album
```

---

### Phase 2: Automation with `src/`
To make the workflow scalable and maintainable, I created the `src/` folder to organize reusable Python scripts:

- `support_call_api.py` → Functions to handle Spotify API calls.  
- `data_manipulation_to_csv.py` → Functions to process and export data into CSV files.  

**Example — Export function:**

```python
def extract_artist(results, genre):
    df = pd.DataFrame(results)
    fileName = f'track_{genre}.csv'
    df.to_csv(fileName, index=False)
```

**Example — Automated loop for multiple genres:**

```python
from src import support_call_api as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz', 'pop', 'classical']

for genre in genre_list:
    track_list, artist_list = ap.get_tracks_and_artists(genre, start_year=2024, end_year=2025)
    dm.load_track(track_list, genre)
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
│   ├── __pycache__
│   ├── data_manipulation_to_csv.py
│   └── support_call_api.py
│
├── .cache/
├── .gitignore
│
├── api.env
├── main.py
│
├── album_jazz.csv
├── album_pop.csv
├── album_rock.csv
│
├── statistics_jazz.csv
├── statistics_pop.csv
├── statistics_rock.csv
│
├── track_classical.csv
├── track_jazz.csv
├── track_pop.csv
├── track_rock.csv
│
├── README.md
└── TODO.md
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

The work started in a **colaborative environment**, we practiced shared code ownership and pair programming. Later, I’ve been iterating on the project independently to raise its quality bar: refactoring code for clarity and reliability, removing sources of error, and automating repeatable tasks (starting with CSV exports via `support_call_api.py` and `data_manipulation_to_csv.py`). I also created and refined the SQL schema and developed the queries that generate decision-ready insights. Throughout, I balanced hands-on coding with leadership—aligning stakeholders, managing delivery risks, and keeping documentation crisp—so the work remains transparent, scalable, and impactful.

### Key contributions 

- **Clear orchestration:** A single `main()` function coordinates the end-to-end flow (API → CSV) per genre in a predictable sequence.  
- **Straightforward configuration:** Years, genres, and paths live in one place, making changes easy and safe to rerun.  
- **Intuitive naming & structure:** Functions and variables reflect their purpose (tracks, albums, stats, biography), so the code reads like the process.  
- **Fewer moving parts:** Reduced unnecessary steps and stitched stages where it made sense, making the pipeline shorter, easier to follow, and faster.  
- **De-dup & rate-limit awareness:** Avoids duplicate calls and includes small pauses, reducing API overhead and keeping requests reliable.  
- **Consistent outputs:** CSV files follow a stable naming pattern and schema, simplifying downstream SQL/analytics and ensuring reproducibility.  
- **Import-friendly design:** The entrypoint pattern lets you reuse pipeline pieces in notebooks or tests without side effects.

---

## 🚀 Next Steps

Currently expanding the project by **automating artist biographies, statistics ingestion** and **SQL** — applying the same ETL approach used for the main datasets to enrich the database further.


