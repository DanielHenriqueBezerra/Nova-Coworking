import "./AgendaDia.css";

export default function AgendaDia({ salas, reservas }) {
  const horas = Array.from({ length: 14 }, (_, i) => i + 8); // 08 → 21

  function reservasDaSala(salaId) {
    return reservas.filter(r => r.sala_id === salaId);
  }

  function calcularEstilo(reserva) {
    const inicio = new Date(reserva.data_reserva);
    const horaInicio = inicio.getHours();
    const minutosInicio = inicio.getMinutes();

    const top = ((horaInicio - 8) * 60 + minutosInicio) * 1;
    const height = 120; // 2 horas padrão (backend)

    return {
      top: `${top}px`,
      height: `${height}px`
    };
  }

  return (
    <div className="agenda">
      <div className="agenda-header">
        <div className="agenda-col hora" />
        {salas.map(sala => (
          <div key={sala.id} className="agenda-col">
            {sala.nome}
          </div>
        ))}
      </div>

      <div className="agenda-body">
        <div className="agenda-col hora">
          {horas.map(h => (
            <div key={h} className="hora-slot">
              {h}:00
            </div>
          ))}
        </div>

        {salas.map(sala => (
          <div key={sala.id} className="agenda-col sala-col">
            {horas.map(h => (
              <div key={h} className="hora-slot" />
            ))}

            {reservasDaSala(sala.id).map(reserva => (
              <div
                key={reserva.id}
                className="reserva-bloco"
                style={calcularEstilo(reserva)}
              >
                <strong>Reservado</strong>
                <br />
                {new Date(reserva.data_reserva).toLocaleTimeString([], {
                  hour: "2-digit",
                  minute: "2-digit"
                })}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

