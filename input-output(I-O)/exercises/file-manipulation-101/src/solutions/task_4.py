"""Move files to a different directory"""
import os 

ROOT = os.getcwd()
DATA_ROOT = os.path.join(ROOT, 'src/data/initial')

def classify(cat_dict):
    for dir, files in cat_dict.items():
        for file in files:
            os.rename(f"{DATA_ROOT}/{file}",
                      f"{DATA_ROOT}/{dir}/{file}")


categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}

classify(categories)
