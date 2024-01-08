from sklearn.metrics.pairwise import cosine_similarity
from model_manager import Embedder
from datetime import date
import word_getter

# Obtener la fecha actual

# Cargar el modelo SentenceTransformer
model = Embedder()
DAY_WORD = None
DAY = None
DAY_EMBEDDING = None

def get_score(text):
    user_embedding = model.encode_sentences([text])
    similarity_score = cosine_similarity(get_day_emedding(), user_embedding)[0][0]
    return int((similarity_score*10000))



def get_day_emedding():
    global DAY, DAY_WORD, DAY_EMBEDDING
    if DAY  == None or DAY != date.today():
        DAY = date.today()
        DAY_WORD = word_getter.get_word(DAY).lower()
        DAY_EMBEDDING = model.encode_sentences([DAY_WORD])
        
    return DAY_EMBEDDING    

