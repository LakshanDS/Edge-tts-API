from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
from Edge_tts import generator

app = FastAPI()

class Request(BaseModel):
    text: str = "I will Make your text Speak!"
    voice: str = "en-US-BrianMultilingualNeural"
    rate: str = "+7%"
    world_in_cue: int = 1

@app.post("/generate")
async def generate(request: Request):
    try:
        result = await generator(request.text, request.voice, request.rate, request.world_in_cue)
        return FileResponse(result, media_type='application/octet-stream', filename="Result.zip")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,
        host="0.0.0.0",
        port=8000)