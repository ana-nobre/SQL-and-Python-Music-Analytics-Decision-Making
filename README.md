# SQL-and-Python-Music-Analytics-Decision-Making

This project was developed to combine **Python** and **SQL** for extracting, organizing, and analyzing real-world music data.

The work began in a **cross-functional team environment**, where I led scope alignment and established the initial API strategy. We worked with shared code ownership and pair programming to accelerate delivery and maintain high standards.

I then advanced the work independently, consolidating the pipeline end-to-end: automating data extraction, designing the SQL schema, and developing queries that delivered decision-ready insights. Along the way, I combined hands-on coding with leadership responsibilities—facilitating stakeholder alignment, managing delivery risks, and ensuring clear documentation—so the project remained transparent, scalable, and impactful.

---

## 📌 Objectives

- Consolidate Python and SQL knowledge in a real-world project.  
- Automate data extraction from music APIs (Spotify and Last.fm).  
- Design and populate a relational database using SQL.  
- Perform analysis through SQL queries to answer business-driven questions.  
- Apply Agile principles with iterative sprints, including daily stand-ups, sprint reviews, and retrospectives to maintain alignment, inspect progress, and continuously improve.

---

## 🔄 Project Phases

### Phase 1: Data Extraction
- Used the **Spotify Web API** to retrieve information about tracks, albums, artists, and release years.  
- Focused on the period **2016–2020** across selected genres (e.g., Rock, Pop, Jazz).  
- Enriched dataset with **Last.fm API** to capture popularity and play statistics.  

**Example: Python function to extract tracks by genre and year**

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
As part of the individual continuation of the project, I created the `src/` folder to organize reusable Python scripts:  

- `support_call_API.py` → Functions to handle Spotify API calls.  
- `data_manipulation.py` → Functions to process and export data.  

This modular approach allowed me to **automate the extraction and saving of CSV files for multiple genres** at once.  

**Example: Data manipulation function**

```python
def extract_artist(results, genre):
    df = pd.DataFrame(results)
    fileName = f'track_{genre}.csv'
    df.to_csv(fileName, index=False)
```

**Example: Automated loop using `src/` modules**

```python

from src import support_call_API as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz']
for genre in genre_list:
    resultados, artist_list = ap.call(genre)
    dm.extract_artist(resultados, genre)
```

This improved workflow ensures new genres can be added by simply extending `genre_list`, making the process scalable and reproducible.  

---

### Phase 3: Database Design and Storage
- Designed a relational schema in **MySQL** to store extracted data.  
- Created tables for **artists, tracks, albums, genres, and popularity metrics**.  
- Inserted and validated the data, ensuring referential integrity and avoiding duplicates.  

**Example: Environment setup for API authentication**

```python
env_path = 'api.env' 
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("CLIENT_ID or CLIENT_SECRET not found in environment variables. "
                     "Please check your api.env file and path.")
```

---

### Phase 4: Analysis and Decision-Making
Key business questions explored with SQL queries:  

- Which artist released the most albums?  
- Which genre shows the highest popularity?  
- In which year were the most albums released?  
- Which track is the top‑ranked by popularity?  
- Which artist accumulates the highest overall rating?  
- Which countries or regions show the highest concentration of listener activity (using regional endpoints or metadata)?

With these extended queries, we could identify collaboration patterns between artists and understand geographic differences in popularity when the API provides regional data.  

---

## 🌍 International vs Local Data

- **Spotify API**: The `/search` endpoint used in this project queries the **global Spotify catalog**, unless a `market` parameter is specified. Without a market filter, results are generally international, not limited to Spain.  
- **Last.fm API**: By default, results are also global. However, Last.fm offers endpoints with country filters (e.g., `geo.getTopArtists`), which can be used to retrieve **country‑specific popularity rankings**.  

This means the code implemented here works with **international data by default**, while also allowing for extensions into regional analysis.  

---

## 📂 Repository Structure

```
SQL-AND-PYTHON-MUSIC-ANALYTICS-DECISION-MAKING/
│
├── Jupyter Notebooks/
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
│   ├── bbdmusicproject.sql
│   ├── bbdmusicproject2.sql
│   ├── bbdmusicprojectA.sql
│   ├── consultas-final-queries.sql
│   └── Spotfy-Creacion-BBDD.sql
│
├── src/
│   ├── data_manipulation.py
│   └── support_call_API.py
│
├── .cache/
├── .gitignore
├── api.env
├── main.py
├── README.md
│
├──  Datasets/
├── jazz_artists.csv
├── track_jazz.csv
└── track_rock.csv
```

---

## 📅 Agile Workflow

- Work planned in **2-week sprints** with backlog tracking, daily stand-ups, sprint reviews, and retrospectives.  
- Early progress was documented as a team → later iterations were continued individually.  
- Challenges and learnings were continuously documented at the end of each sprint to drive improvement.  

---

## ✅ Key Deliverables

- Automated data extraction scripts (Python).  
- SQL schema and database population.  
- Analytical SQL queries answering music industry questions.  
- Clear documentation and repository organization for reproducibility. 
- Analytical SQL queries that not only answer music industry questions (e.g., releases, popularity, collaborations) but also generate actionable insights to support product strategy, marketing decisions, and content planning.


---

## 📊 Final Presentation

The project concludes with a presentation including:  
- Overview of objectives and methodology.  
- Demonstration of Python automation and SQL analysis.  
- Key findings and insights for decision-making.  
- Reflections on challenges and learning outcomes.  

---
