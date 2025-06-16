import { createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { decodeJwtPayload } from "../utils/token";
import { useAlert } from "./AlertContext";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState({ user: null, loading: true });
  const { showAlert } = useAlert();
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("jwt_token");
    setAuth({ user: null, loading: false });
    navigate("/");
  };
  
  const loginUser = (jwt_token) => {
    const payload = decodeJwtPayload(jwt_token);
    localStorage.setItem("jwt_token", jwt_token);
    setAuth({ user: { "role": payload.role }, loading: false });
    if (payload.role === "user") navigate("/dashboard");
    else if (payload.role === "admin") navigate("/admin/dashboard");
    else {
      showAlert("Access denied. Invalid role.", "critical", 3000);
      navigate("/");
    }
  };
  
  useEffect(() => {
    const jwt_token = localStorage.getItem("jwt_token");
    if (!jwt_token || jwt_token === undefined) {
      setAuth({ user: null, loading: false });
    }
    else {
      try{
        const payload = decodeJwtPayload(jwt_token);
        setAuth({ user: { "role": payload.role }, loading: false });
      }
      catch(err){
        localStorage.removeItem("jwt_token");
      }
    }
  }, []);

  return (
    <AuthContext.Provider value={{ ...auth, loginUser, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);