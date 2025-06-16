import React from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const HandleLoginNavigation = () => {
    navigate("/login");
  }
  return (
    <button onClick={HandleLoginNavigation}>Login</button>
  )
}

export default HomePage;