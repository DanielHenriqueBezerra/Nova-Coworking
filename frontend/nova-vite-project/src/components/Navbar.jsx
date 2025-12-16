import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <aside className="Navbar">
      
      <div className="navbar-header">
        <img
          src="/iconSupernova.png"
          alt="Nova Coworking"
          className="navbar-logo"
        />
        <h2>Nova Coworking</h2>
      </div>

      <nav>
        <Link to="/">Dashboard</Link>
        <Link to="/usuarios">Usuários</Link>
        <Link to="/salas">Salas</Link>
        <Link to="/reservas">Reservas</Link>
      </nav>
    </aside>
  );
}
