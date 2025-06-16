import React from "react";
import AppRoutes from "./routes/AppRoutes";
import { ThemeProvider } from "./context/ThemeContext";
import { AlertProvider } from "./context/AlertContext";
import { AuthProvider } from "./context/AuthContext";

const AlertDisplay = React.lazy(() => import("./components/global/Alert"));

function App() {
  return (
    <AlertProvider>
      <AuthProvider>
      <ThemeProvider>
        <AlertDisplay />
        <AppRoutes />
      </ThemeProvider>
      </AuthProvider>
    </AlertProvider>
  );
}

export default App;
