
from database import Base, engine
from models.usuario import Usuario
from models.sala import Sala
from models.reserva import Reserva

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso! / Tables created successfully!")
