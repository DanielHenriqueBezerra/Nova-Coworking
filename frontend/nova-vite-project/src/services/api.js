import axios from "axios";

/*
Centraliza a comunicação com o backend
*/
const api = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export default api;
