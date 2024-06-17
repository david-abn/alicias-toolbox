from typing import Dict
from template_text import (
    body_language,
    voice,
    speed,
    interactions,
    recall,
    q_and_a
)

def selections() -> list[Dict[str, str]]:
    b = body_language
    v = voice
    s = speed
    i = interactions
    r = recall
    q = q_and_a
    
    students = [
        {
            "student": "David",
            "tutor": "Mina",
            "body_language": b['2'],
            "voice": v['1'],
            "speed": s['1'],
            "interactions": i['1'],
            "recall": r['1'],
            "q_and_a": q['1']
        },
    {
            "student": "Emina",
            "tutor": "Alicia",
            "body_language": b['1'],
            "voice": v['1'],
            "speed": s['1'],
            "interactions": i['1'],
            "recall": r['1'],
            "q_and_a": q['1']
        },
    {
            "student": "Emina",
            "tutor": "Alicia",
            "body_language": b['1'],
            "voice": v['1'],
            "speed": s['1'],
            "interactions": i['1'],
            "recall": r['1'],
            "q_and_a": q['1']
        },
    ]        
    return students