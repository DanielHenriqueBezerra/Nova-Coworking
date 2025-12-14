import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <aside className="Navbar">
      <h2>Nova Coworking</h2>

      <nav>
        <Link to="/">Dashboard</Link>
        <Link to="/usuarios">Usuários</Link>
        <Link to="/salas">Salas</Link>
        <Link to="/reservas">Reservas</Link>
      </nav>
    </aside>
  );
}
