from pydantic import BaseModel
from datetime import date, timedelta
from enum import Enum
from sqlalchemy import Column, String, Date, Integer
from app.database.database import Base


class ServicesStatus(str, Enum):
    """Enumeration representing the status of a ServicesRequest."""
    active = "active"
    completed = "completed"


class ServicesRequest(Base):
    __tablename__ = "services_requests"

    id: int = Column(Integer, primary_key=True, index=True)
    service_reference: str = Column(String)
    workshop_reference: str = Column(String)
    car_tools_reference: str = Column(String)
    car_issues_text: str = Column(String)
    maintenance_date: date = Column(Date)
    next_maintenance_date: date = Column(Date)
    status: str = Column(String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.maintenance_date:
            self.calculate_next_maintenance_date()

    def calculate_next_maintenance_date(self):
        self.next_maintenance_date = self.maintenance_date + timedelta(days=6*30)


class ServicesRequestIn(BaseModel):
    service_reference: str
    workshop_reference: str
    car_tools_reference: str
    car_issues_text: str
    maintenance_date: date
    next_maintenance_date: date
    status: ServicesStatus


class ServicesRequestOut(BaseModel):
    id: int
    service_reference: str
    workshop_reference: str
    car_tools_reference: str
    car_issues_text: str
    maintenance_date: date
    next_maintenance_date: date
    status: ServicesStatus
