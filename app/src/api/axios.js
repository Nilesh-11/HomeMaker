import axios from 'axios';
import { BACKEND_URL } from '../config/config';

const axiosInstance = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('JWT-Token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    const { response } = error;
    if (!response) {
      console.error('Network error or server not reachable');
    } else {
      switch (response.status) {
        case 400:
          console.warn('Bad request:', response.data.message);
          break;
        case 401:
          console.warn('Unauthorized: Logging out user');
          break;
        case 403:
          console.warn('Forbidden');
          break;
        case 500:
          console.error('Server error');
          break;
        default:
          console.warn(`Unexpected error: ${response.status}`);
      }
    }

    return Promise.reject(error);
  }
);

export default axiosInstance;
