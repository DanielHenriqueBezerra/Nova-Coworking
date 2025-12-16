import { useEffect, useState } from "react";
import api from "../services/api";
import Navbar from "../components/Navbar";
import AgendaDia from "../components/AgendaDia";

function toArray(data) {
  return Array.isArray(data) ? data : [];
}

export default function Reservas() {
  const [usuarios, setUsuarios] = useState([]);
  const [salas, setSalas] = useState([]);
  const [reservas, setReservas] = useState([]);

  const [usuarioId, setUsuarioId] = useState("");
  const [salaId, setSalaId] = useState("");
  const [dataReserva, setDataReserva] = useState("");
  const [duracao, setDuracao] = useState(2);

  const [mensagem, setMensagem] = useState("");
  const [erro, setErro] = useState("");

  useEffect(() => {
    async function carregar() {
      try {
        const [u, s, r] = await Promise.all([
          api.get("/usuarios/"),
          api.get("/salas/"),
          api.get("/reservas/"),
        ]);

        setUsuarios(toArray(u.data));
        setSalas(toArray(s.data));
        setReservas(toArray(r.data));
      } catch (e) {
        const detail = e?.response?.data?.detail;
        setErro(detail || "Erro ao carregar dados");
      }
    }
    carregar();
  }, []);

  function getNomeUsuario(id) {
    const usuario = usuarios.find((u) => Number(u.id) === Number(id));
    return usuario ? usuario.nome : "Usuário não encontrado";
  }

  function getNomeSala(id) {
    const sala = salas.find((s) => Number(s.id) === Number(id));
    return sala ? sala.nome : "Sala não encontrada";
  }

  function formatarPeriodo(dataISO, duracaoStr) {
    if (!dataISO || !duracaoStr) return "-";

    const inicio = new Date(dataISO);
    const horas = parseInt(String(duracaoStr).replace("h", ""), 10) || 0;

    const fim = new Date(inicio);
    fim.setHours(inicio.getHours() + horas);

    const data = inicio.toLocaleDateString("pt-BR");
    const horaInicio = inicio.toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" });
    const horaFim = fim.toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" });

    return `${data} | ${horaInicio} → ${horaFim}`;
  }

  async function recarregarReservas() {
    const r = await api.get("/reservas/");
    setReservas(toArray(r.data));
  }

  async function criarReserva(e) {
    e.preventDefault();
    setMensagem("");
    setErro("");

    try {
      await api.post("/reservas/", {
        usuario_id: Number(usuarioId),
        sala_id: Number(salaId),
        data_reserva: dataReserva,
        status: `${duracao}h`,
        observacao: "",
      });

      setMensagem("Reserva criada com sucesso");

      setUsuarioId("");
      setSalaId("");
      setDataReserva("");
      setDuracao(2);

      await recarregarReservas();
    } catch (e) {
      setErro(e?.response?.data?.detail || "Erro ao criar reserva");
    }
  }

  async function excluirReserva(id) {
    setMensagem("");
    setErro("");

    if (!window.confirm("Excluir reserva?")) return;

    try {
      await api.delete(`/reservas/${id}`);
      setReservas((prev) => prev.filter((r) => Number(r.id) !== Number(id)));
      setMensagem("Reserva excluída com sucesso");
    } catch (e) {
      setErro(e?.response?.data?.detail || "Erro ao excluir reserva");
    }
  }

  return (
    <div className="app-container">
      <Navbar />

      <main className="main-content reservas-page">
        <div className="page-container">
          <h1 className="page-title">Reservas</h1>

          {mensagem && <div className="alert success">{mensagem}</div>}
          {erro && <div className="alert error">{erro}</div>}

          <div className="reservas-layout">
            <div className="reservas-form">
              <form onSubmit={criarReserva} className="card">
                <select value={usuarioId} onChange={(e) => setUsuarioId(e.target.value)} required>
                  <option value="">Selecione o Usuário</option>
                  {usuarios.map((u) => (
                    <option key={u.id} value={u.id}>
                      {u.nome}
                    </option>
                  ))}
                </select>

                <select value={salaId} onChange={(e) => setSalaId(e.target.value)} required>
                  <option value="">Selecione a Sala</option>
                  {salas.map((s) => (
                    <option key={s.id} value={s.id}>
                      {s.nome}
                    </option>
                  ))}
                </select>

                <input
                  type="datetime-local"
                  value={dataReserva}
                  onChange={(e) => setDataReserva(e.target.value)}
                  required
                />

                <select value={duracao} onChange={(e) => setDuracao(Number(e.target.value))} required>
                  {[2, 3, 4, 5, 6, 8, 10, 12].map((h) => (
                    <option key={h} value={h}>
                      {h} horas
                    </option>
                  ))}
                </select>

                <button type="submit">Criar Reserva</button>
              </form>
            </div>

            <div className="reservas-tabela">
              <table>
                <thead>
                  <tr>
                    <th>Usuário</th>
                    <th>Sala</th>
                    <th>Período</th>
                    <th>Duração</th>
                    <th>Ação</th>
                  </tr>
                </thead>
                <tbody>
                  {reservas.length === 0 ? (
                    <tr>
                      <td colSpan="5" style={{ textAlign: "center", opacity: 0.8 }}>
                        Nenhuma reserva cadastrada
                      </td>
                    </tr>
                  ) : (
                    reservas.map((r) => (
                      <tr key={r.id}>
                        <td>{getNomeUsuario(r.usuario_id)}</td>
                        <td>{getNomeSala(r.sala_id)}</td>
                        <td>{formatarPeriodo(r.data_reserva, r.status)}</td>
                        <td>{r.status}</td>
                        <td>
                          <button className="danger" onClick={() => excluirReserva(r.id)}>
                            Excluir
                          </button>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>

            <div className="reservas-agenda">
              <h2>Agenda do Dia</h2>
              <AgendaDia salas={salas} reservas={reservas} />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
