"""
GSMT Ver 7.0 - Clean Railway Build
Rebuilt from scratch for guaranteed Railway compatibility
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Create FastAPI application
app = FastAPI(
    title="GSMT Ver 7.0 API",
    description="Global Stock Market Tracker - Clean Build",
    version="7.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint - API status"""
    return {
        "name": "GSMT Ver 7.0 API",
        "version": "7.0.0",
        "status": "healthy",
        "description": "Global Stock Market Tracker",
        "deployment": "railway",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for Railway"""
    return {
        "status": "healthy",
        "service": "GSMT Ver 7.0 Backend",
        "version": "7.0.0",
        "timestamp": "2025-01-03T00:00:00Z",
        "deployment": "railway"
    }

@app.get("/test")
async def test_endpoint():
    """Test endpoint to verify deployment"""
    return {
        "test": "success",
        "message": "GSMT Ver 7.0 API is working correctly",
        "railway": "deployment successful",
        "features": [
            "FastAPI application",
            "CORS enabled",
            "Health checks",
            "API documentation"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)