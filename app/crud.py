from sqlalchemy.orm import Session

from . import models, schemas


def get_plato(db: Session, plato_id: int):
    return db.query(models.Plato).filter(models.Plato.id == plato_id).first()


def get_platos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Plato).offset(skip).limit(limit).all()


def create_plato(db: Session, plato_in: schemas.PlatoCreate):
    plato = models.Plato(**plato_in.model_dump())
    db.add(plato)
    db.commit()
    db.refresh(plato)
    return plato


def update_plato(db: Session, plato: models.Plato, plato_in: schemas.PlatoUpdate):
    data = plato_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(plato, field, value)
    db.add(plato)
    db.commit()
    db.refresh(plato)
    return plato


def delete_plato(db: Session, plato: models.Plato):
    db.delete(plato)
    db.commit()
