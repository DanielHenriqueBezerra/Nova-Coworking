# Importa o objeto Base e engine do arquivo database.py
# Import Base and engine object from database.py
from database import Base, engine

# Importa os modelos que representam as tabelas do banco de dados
# Import models that represent database tables
from models.usuario import Usuario
from models.sala import Sala
from models.reserva import Reserva

# Cria todas as tabelas definidas nos models no banco de dados
# Create all tables defined in models in the database
Base.metadata.create_all(bind=engine)

# Mensagem para confirmar que as tabelas foram criadas
# Message to confirm that tables were created
print("Tabelas criadas com sucesso! / Tables created successfully!")
