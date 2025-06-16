// import { useEffect } from "react";
// import { GOOGLE_CLIENT_ID } from "../config/config";

// const GoogleLogin = ({ onLogin }) => {
//   useEffect(() => {
//     if (!window.google || !document.getElementById("google-signin-btn")) return;

//     const handleCredentialResponse = async (response) => {
//       const idToken = response.credential;

//       try {
//         const res = await fetch("http://localhost:8000/v1/auth/google/login", {
//           method: "POST",
//           headers: { "Content-Type": "application/json" },
//           body: JSON.stringify({ token: idToken }),
//         });

//         const data = await res.json();
//         if (res.ok) {
//           localStorage.setItem("jwt", data.token);
//           onLogin({ type: "ok", message: "Logged in successfully!" });
//         } else {
//           console.error("Backend error:", data);
//           onLogin({ type: "error", message: data.message || "Login failed!" });
//         }
//       } catch (err) {
//         console.error("Request error:", err);
//         onLogin({ type: "error", message: "Request failed. Try again." });
//       }
//     };

//     window.google.accounts.id.initialize({
//       client_id: GOOGLE_CLIENT_ID,
//       callback: handleCredentialResponse,
//     });

//     window.google.accounts.id.renderButton(
//       document.getElementById("google-signin-btn"),
//       { theme: "outline", size: "large" }
//     );

//     window.google.accounts.id.prompt();
//   }, [onLogin]);

//   return <div id="google-signin-btn"></div>;
// };

// export default GoogleLogin;


// let tokenClient;

// export const authenticateWithGoogle = () => {
//   return new Promise((resolve, reject) => {
//     try {
//       if (!tokenClient) {
//         tokenClient = window.google.accounts.oauth2.initTokenClient({
//           client_id: GOOGLE_CLIENT_ID,
//           scope: "openid email profile",
//           callback: async (response) => {
//             if (response.error) {
//               console.error("Token error:", response);
//               alert("Login failed!");
//               return reject({ type: "error", message: "Google Server error" });
//             }
//             console.log(response);
//             const idToken = response.access_token;

//             try {
//               const res = await axiosInstance.post('/v1/auth/google/login', {
//                 token: idToken,
//               });
//               const { jwtToken, user } = res.data;
//               localStorage.setItem('JWT-Token', jwtToken);

//               resolve({ type: "ok", message: "Login successful", user });
//             } catch (apiErr) {
//               console.error("Backend login failed:", apiErr);
//               reject({
//                 type: "error",
//                 message: apiErr.response?.data?.message || "Login failed",
//               });
//             }
//           },
//         });
//       }

//       tokenClient.requestAccessToken();
//     } catch (err) {
//       console.error("Unexpected error:", err);
//       reject({ type: "error", message: "An unexpected error occurred" });
//     }
//   });
// };

