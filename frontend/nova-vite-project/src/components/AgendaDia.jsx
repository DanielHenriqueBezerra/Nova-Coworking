export default function AgendaDia({ salas, reservas }) {
  if (!Array.isArray(salas) || !Array.isArray(reservas)) {
    return <p>Carregando agenda...</p>;
  }

  return (
    <div>
      {/* renderização segura */}
    </div>
  );
}
