from fastapi import FastAPI

app = FastAPI(title='SmartSchool API', version='0.1.0', docs_url='/docs', redoc_url='/redoc')

@app.get('/health')
def health():
    return {'status':'ok'}

@app.get('/api/v1/health')
def v1_health():
    return {'status':'ok','version':'1.0.0'}

