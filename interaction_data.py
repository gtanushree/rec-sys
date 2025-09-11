from pydantic import BaseModel

class Attributes(BaseModel):
    student_id: str
    video_title: str
    video_link: str
    video_description: str
    video_tags: str
    interaction_type: str