import { useEffect, useState } from "react";
import api from "../services/api";
import Navbar from "../components/Navbar";
import Card from "../components/Card";

export default function Dashboard() {
  const [totalUsuarios, setTotalUsuarios] = useState(0);
  const [totalSalas, setTotalSalas] = useState(0);
  const [totalReservas, setTotalReservas] = useState(0);

  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState("");

  useEffect(() => {
    async function carregarDashboard() {
      try {
        const [usuariosRes, salasRes, reservasRes] = await Promise.all([
          api.get("/usuarios/"),
          api.get("/salas/"),
          api.get("/reservas/")
        ]);

        setTotalUsuarios(usuariosRes.data.length);
        setTotalSalas(salasRes.data.length);
        setTotalReservas(reservasRes.data.length);
      } catch (err) {
        console.error(err);
        setErro("Não foi possível carregar os dados do sistema.");
      } finally {
        setLoading(false);
      }
    }

    carregarDashboard();
  }, []);

  return (
    <div className="app-container">
      <Navbar />

      <main className="main-content">
        <div className="page-container dashboard-page">

          <h1>Dashboard</h1>

          {/* LOADING */}
          {loading && (
            <div className="alert info">
              Carregando informações do sistema...
            </div>
          )}

          {/* ERRO */}
          {erro && (
            <div className="alert error">
              {erro}
            </div>
          )}

          {/* CONTEÚDO */}
          {!loading && !erro && (
            <>
              <div className="cards dashboard-cards">
                <Card titulo="Usuários cadastrados" valor={totalUsuarios} />
                <Card titulo="Salas disponíveis" valor={totalSalas} />
                <Card titulo="Reservas registradas" valor={totalReservas} />
              </div>

              <div className="dashboard-text">
                <p>
                  Este painel apresenta um resumo geral do sistema de gestão de
                  salas do coworking, permitindo uma visão rápida da ocupação e
                  utilização dos espaços.
                </p>
              </div>
            </>
          )}

        </div>
      </main>
    </div>
  );
}
