import "./AgendaDia.css";

export default function AgendaDia({ salas, reservas }) {
  const horas = Array.from({ length: 14 }, (_, i) => i + 8); // 08 → 21
  const hoje = new Date();

  function mesmaData(dataISO) {
    const d = new Date(dataISO);
    return (
      d.getFullYear() === hoje.getFullYear() &&
      d.getMonth() === hoje.getMonth() &&
      d.getDate() === hoje.getDate()
    );
  }

  function reservasDaSala(salaId) {
    return reservas.filter(
      r => r.sala_id === salaId && mesmaData(r.data_reserva)
    );
  }

  function calcularEstilo(reserva) {
    const inicio = new Date(reserva.data_reserva);
    const horaInicio = inicio.getHours();
    const minutosInicio = inicio.getMinutes();

    const duracaoHoras =
      parseInt(String(reserva.status).replace("h", ""), 10) || 2;

    const top = ((horaInicio - 8) * 60 + minutosInicio) * 1;
    const height = duracaoHoras * 60; // 1h = 60px

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
                {new Date(reserva.data_reserva).toLocaleTimeString("pt-BR", {
                  hour: "2-digit",
                  minute: "2-digit"
                })}
                <br />
                {reserva.status}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
