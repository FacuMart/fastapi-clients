from sqlalchemy.orm import Session
from . import models, schemas

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first() # type: ignore

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    cliente = get_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()

def update_cliente(db: Session, cliente_id: int, cliente_data: schemas.ClienteCreate):
    cliente = get_cliente(db, cliente_id)
    if cliente:
        for field, value in cliente_data.model_dump().items():
            setattr(cliente, field, value)
        db.commit()
        db.refresh(cliente)
        return cliente
    return None
