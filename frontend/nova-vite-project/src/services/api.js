import axios from "axios";

const api = axios.create({
  baseURL: "https://nova-coworking.onrender.com",
});

export default api;
