from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import AnswerCreate, AnswerOut
from app.models import QuestionnaireAnswer, User
from app.utils.scoring import calculate_risk_score
from app.utils.advice import generate_advice
from app.crud import get_db

router = APIRouter()

@router.post("/answer", response_model=AnswerOut)
def submit_answer(user_id: int, answer: AnswerCreate, db: Session = Depends(get_db)):
    score = calculate_risk_score(answer.question, answer.answer)
    new_answer = QuestionnaireAnswer(
        user_id=user_id,
        question=answer.question,
        answer=answer.answer,
        score=score
    )
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)

    advice = generate_advice(answer.question.lower(), score)
    # Here, you can store or return advice too
    return new_answer
