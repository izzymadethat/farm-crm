from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Contact
from app.types.contact import ContactItem, ContactResponse 

router = APIRouter()

@router.get("/contacts", response_model=list[ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    contacts = db.query(Contact).all()
    return contacts

@router.get("/contacts/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        return contact
    return {"error": "Contact not found"}, 404

@router.post("/contacts")
def create_contact(contact: ContactItem, db: Session = Depends(get_db)):
    new_contact = Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"contact": new_contact}