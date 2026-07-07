from pydantic import BaseModel


class AIRequest(BaseModel):
    vehicle_id: int