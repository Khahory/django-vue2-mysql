import axios from "axios";

const getAPI = axios.create({
    baseURL: "http://192.168.0.5:8000/",
    timeout: 1000
})

export { getAPI }