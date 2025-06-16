import React from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const HandleLoginNavigation = () => {
    navigate("/");
}

const HandleLogOutNavigation = () => {
    navigate("/");
  }
  return (
    <div>
        <button onClick={HandleLoginNavigation}>Home</button>
        <button onClick={HandleLogOutNavigation}>LogOut</button>
    </div>
  )
}

export default HomePage;