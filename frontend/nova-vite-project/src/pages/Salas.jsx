import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import Navbar from "../components/Navbar";

import img1 from "../imagens/imagem1.jpg";
import img2 from "../imagens/imagem2.jpg";
import img3 from "../imagens/imagem3.jpg";

const imagens = [img1, img2, img3];

export default function Salas() {
  const [salas, setSalas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    async function carregarSalas() {
      try {
        const res = await api.get("/salas/");
        setSalas(res.data);
      } catch {
        setErro("Erro ao carregar salas.");
      } finally {
        setLoading(false);
      }
    }

    carregarSalas();
  }, []);

  function reservarSala(salaId) {
    navigate("/reservas", {
      state: { salaId }
    });
  }

  return (
    <div className="app-container">
      <Navbar />

      <main className="main-content">
        <div className="page-container">
          <h1>Salas</h1>

         
          {loading && <p>Carregando salas...</p>}

          
          {erro && <div className="alert error">{erro}</div>}

          
          {!loading && !erro && (
            <div className="salas-grid">
              {salas.map((sala, index) => (
                <div className="card sala" key={sala.id}>
                  <img
                    src={imagens[index % imagens.length]}
                    alt={`Sala ${sala.nome}`}
                  />

                  <h3>{sala.nome}</h3>

                  <p>
                    <strong>Capacidade:</strong> {sala.capacidade}
                  </p>

                  {sala.recursos && <p>{sala.recursos}</p>}

                  <button onClick={() => reservarSala(sala.id)}>
                    Reservar
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
