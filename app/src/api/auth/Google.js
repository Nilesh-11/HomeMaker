import { useEffect } from "react";
import { GOOGLE_CLIENT_ID } from "../../config/config";
import axiosInstance from "../axios";
import { useAuth } from "../../context/AuthContext";
import { useAlert } from "../../context/AlertContext";
import { statusMessages } from "../../utils/request"

const GoogleLogin = ({ onLogin }) => {
  const { loginUser } = useAuth();
  const { showAlert } = useAlert();

  useEffect(() => {
    if (!window.google || !document.getElementById("google-signin-btn")) return;

    const handleCredentialResponse = async (response) => {
      const idToken = response.credential;

      try {
        const res = await axiosInstance.post('/v1/auth/google/login', {
          token: idToken,
        });
        if (res.status === 200) {
          showAlert("Login Successful", "success", 3000);
        }
        else {
          showAlert(statusMessages[res.status], "error", 3000);
        }
        console.log(res.headers['x-jwt-token']);
        const jwtToken = res.headers['x-jwt-token'];
        loginUser(jwtToken)
      } catch (err) {
        console.error("Request error:", err);
      }
    };

    window.google.accounts.id.initialize({
      client_id: GOOGLE_CLIENT_ID,
      callback: handleCredentialResponse,
    });

    window.google.accounts.id.renderButton(
      document.getElementById("google-signin-btn"),
      { theme: "outline", size: "large" }
    );

    window.google.accounts.id.prompt();
  }, [onLogin]);

  return <div id="google-signin-btn"></div>;
};

export default GoogleLogin;
