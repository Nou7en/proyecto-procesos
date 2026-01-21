from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_crud_plato():
    create_payload = {
        "nombre": "Ensalada",
        "descripcion": "Fresca",
        "precio": 5.5,
        "disponible": True,
    }

    response = client.post("/platos", json=create_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Ensalada"
    plato_id = data["id"]

    response = client.get(f"/platos/{plato_id}")
    assert response.status_code == 200

    response = client.put(
        f"/platos/{plato_id}", json={"precio": 6.0, "disponible": False}
    )
    assert response.status_code == 200
    assert response.json()["precio"] == 6.0

    response = client.get("/platos")
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.delete(f"/platos/{plato_id}")
    assert response.status_code == 204

    response = client.get(f"/platos/{plato_id}")
    assert response.status_code == 404
