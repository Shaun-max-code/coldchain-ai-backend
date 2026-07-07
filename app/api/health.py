from fastapi import APIRouter

router = APIRouter(
    prefix="/api/health",
    tags=["Health"],
)


@router.get("/")
def health():
    return {
        "status": "healthy",
        "service": "CryoGuard Backend",
        "version": "1.0.0"
    }