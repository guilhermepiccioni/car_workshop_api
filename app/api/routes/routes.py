from fastapi import HTTPException, Path, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from app.database.database import SessionLocal
from app.models.models import ServicesRequestOut, ServicesRequestIn, ServicesRequest


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routes
@router.post("/services_requests/", response_model=ServicesRequestOut)
def create_service_request(
    service_request: ServicesRequestIn,
    db: Session = Depends(get_db)
):
    """Create a new medication request in the database."""
    db_request = ServicesRequest(**service_request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


@router.get("/services_requests/", response_model=List[ServicesRequestOut])
def get_service_requests(
    status: str = None,
    maintenance_date: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(ServicesRequest)

    if status:
        query = query.filter(ServicesRequest.status == status)
    if maintenance_date:
        query = query.filter(ServicesRequest.maintenance_date >= maintenance_date)

    return query.all()


@router.get("/services_requests/{request_id}", response_model=ServicesRequestOut)
def get_single_service_request(
    request_id: str = Path(..., description="The ID of the service request to retrieve"),
    db: Session = Depends(get_db)
):

    db_request = db.query(ServicesRequest).filter(ServicesRequest.id == request_id).first()

    if db_request is None:
        raise HTTPException(status_code=404, detail="Service request not found")

    return db_request


@router.patch("/services_requests/{request_id}", response_model=ServicesRequestOut)
def update_service_request(
    request_id: str,
    service_request: ServicesRequestIn,
    db: Session = Depends(get_db)
):

    db_request = db.query(ServicesRequest).filter(ServicesRequest.id == request_id).first()

    if db_request is None:
        raise HTTPException(status_code=404, detail="Service request not found")

    for var, value in service_request.dict(exclude_unset=True).items():
        setattr(db_request, var, value)

    db.commit()
    db.refresh(db_request)
    return db_request
