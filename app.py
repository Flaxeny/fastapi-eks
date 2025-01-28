from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Page</title>
    </head>
    <body>
        <h1>Welcome to FastAPI!</h1>
        <p>This is a simple web page served using FastAPI.</p>
    </body>
    </html>
    """
@app.get("/health", response_class=JSONResponse)
async def health_check():
    return {"status": "healthy", "message": "The FastAPI application is running smoothly."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

