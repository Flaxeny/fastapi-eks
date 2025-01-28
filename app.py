from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Romskor Page</title>
    </head>
    <body>
        <h1>Romskor page</h1>
        <p>FastAPI in EKS Cluster</p>
        <p>Check the <a href="/health">health status</a> of the application.</p>
        <p>Check the <a href="/time">current time</a>while using app.</p>
    </body>
    </html>
    """
@app.get("/health", response_class=JSONResponse)
async def health_check():
    return {"status": "healthy", "message": "The FastAPI application is running smoothly."}

@app.get("/time", response_class=JSONResponse)
async def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=80)

