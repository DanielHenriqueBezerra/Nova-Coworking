import axios from "axios";

const api = axios.create({
  baseURL: "https://nova-coworking.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
