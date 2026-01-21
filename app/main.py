from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD de Platos")


@app.post("/platos", response_model=schemas.Plato, status_code=status.HTTP_201_CREATED)
def crear_plato(plato_in: schemas.PlatoCreate, db: Session = Depends(get_db)):
    return crud.create_plato(db, plato_in)


@app.get("/platos", response_model=list[schemas.Plato])
def listar_platos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_platos(db, skip=skip, limit=limit)


@app.get("/platos/{plato_id}", response_model=schemas.Plato)
def obtener_plato(plato_id: int, db: Session = Depends(get_db)):
    plato = crud.get_plato(db, plato_id)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")
    return plato


@app.put("/platos/{plato_id}", response_model=schemas.Plato)
def actualizar_plato(
    plato_id: int, plato_in: schemas.PlatoUpdate, db: Session = Depends(get_db)
):
    plato = crud.get_plato(db, plato_id)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")
    return crud.update_plato(db, plato, plato_in)


@app.delete("/platos/{plato_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_plato(plato_id: int, db: Session = Depends(get_db)):
    plato = crud.get_plato(db, plato_id)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")
    crud.delete_plato(db, plato)
    return None
