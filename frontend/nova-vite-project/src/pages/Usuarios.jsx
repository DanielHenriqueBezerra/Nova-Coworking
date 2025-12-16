import { useEffect, useState } from "react";
import api from "../services/api";
import Navbar from "../components/Navbar";

export default function Usuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");

  const [loading, setLoading] = useState(true);
  const [mensagem, setMensagem] = useState("");
  const [erro, setErro] = useState("");

  useEffect(() => {
    async function carregarUsuarios() {
      try {
        const res = await api.get("/usuarios/");
        setUsuarios(res.data);
      } catch (err) {
        console.error(err);
        setErro("Erro ao carregar usuários.");
      } finally {
        setLoading(false);
      }
    }

    carregarUsuarios();
  }, []);

  async function criarUsuario(e) {
    e.preventDefault();
    setMensagem("");
    setErro("");

    try {
      await api.post("/usuarios/", null, {
        params: { nome, email, senha }
      });

      setNome("");
      setEmail("");
      setSenha("");
      setMensagem("Usuário cadastrado com sucesso.");

      const res = await api.get("/usuarios/");
      setUsuarios(res.data);
    } catch (err) {
      console.error(err);
      setErro("Erro ao cadastrar usuário.");
    }
  }

  async function excluirUsuario(id) {
    if (!window.confirm("Deseja excluir este usuário?")) return;

    try {
      await api.delete(`/usuarios/${id}`);
      setUsuarios(prev => prev.filter(u => u.id !== id));
    } catch (err) {
      console.error(err);
      setErro("Erro ao excluir usuário.");
    }
  }

  return (
  <div className="app-container">
    <Navbar />

    <main className="main-content">
      <div className="page-container usuarios-page">

        <h1>Usuários</h1>

        {mensagem && <div className="alert success">{mensagem}</div>}
        {erro && <div className="alert error">{erro}</div>}
        {loading && <p>Carregando usuários...</p>}

        
        <section className="usuarios-section">
          <form onSubmit={criarUsuario} className="card usuarios-form">
            <input
              placeholder="Nome completo"
              value={nome}
              onChange={e => setNome(e.target.value)}
              required
            />

            <input
              placeholder="Email"
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
            />

            <input
              placeholder="Senha"
              type="password"
              value={senha}
              onChange={e => setSenha(e.target.value)}
              required
            />

            <button type="submit">Cadastrar Usuário</button>
          </form>
        </section>

        
        <section className="usuarios-section">
          {!loading && usuarios.length === 0 && (
            <p>Nenhum usuário cadastrado.</p>
          )}

          {!loading && usuarios.length > 0 && (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Ações</th>
                  </tr>
                </thead>
                <tbody>
                  {usuarios.map(u => (
                    <tr key={u.id}>
                      <td>{u.nome}</td>
                      <td>{u.email}</td>
                      <td>
                        <button
                          className="danger"
                          onClick={() => excluirUsuario(u.id)}
                        >
                          Excluir
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </section>

      </div>
    </main>
  </div>
)};

