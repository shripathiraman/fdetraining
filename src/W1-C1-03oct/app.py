from fastapi import FastAPI  

app = FastAPI(title="FDE Week 1 API")  

@app.get("/")
def root():
    return {"message": "FDE Week 1 API", "docs": "/docs", "health": "/health"}

@app.get("/health") 

def health():     
    return {"status": "ready", "week": 1} 