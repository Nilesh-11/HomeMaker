import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAlert } from "../context/AlertContext";
// import GoogleLogin from "./GoogleLogin";
import GoogleLogin from "../api/auth/Google";

const LoginPage = () => {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { showAlert } = useAlert();
  const navigate = useNavigate();

  const handleGoogleLoginResult = (result) => {
    setIsSubmitting(false);
    if (result?.type === "ok") {
      showAlert(result.message, 'success', 3000);
      // navigate("/dashboard");
    } else {
      showAlert(result.message, 'error', 3000);
    }
  };

  return (
    <div className="main">
      <h2>Sign in with Google</h2>
      {isSubmitting && <p>Signing in...</p>}
      <GoogleLogin />
    </div>
  );
};

export default LoginPage;
