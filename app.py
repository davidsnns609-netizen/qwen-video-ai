import os
from io import BytesIO
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from huggingface_hub import InferenceClient

app = FastAPI(title="Qwen Video AI")
app.mount("/static", StaticFiles(directory="static"), name="static")

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=5, max_length=1500)

@app.get("/")
def home():
    from fastapi.responses import FileResponse
    return FileResponse("static/index.html")

@app.post("/api/generate")
def generate_video(data: GenerateRequest):
    token = os.getenv("HF_TOKEN")
    if not token:
        raise HTTPException(
            status_code=503,
            detail="لم يتم إعداد مفتاح Hugging Face بعد. اتبع خطوات README."
        )
    try:
        client = InferenceClient(provider="fal-ai", api_key=token, timeout=900)
        video_bytes = client.text_to_video(
            data.prompt,
            model="Wan-AI/Wan2.2-TI2V-5B",
        )
        if not video_bytes:
            raise RuntimeError("لم تُرجع الخدمة ملف فيديو.")
        return StreamingResponse(
            BytesIO(video_bytes),
            media_type="video/mp4",
            headers={"Content-Disposition": 'inline; filename="qwen-video.mp4"'}
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"تعذر إنشاء الفيديو: {str(exc)[:500]}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
