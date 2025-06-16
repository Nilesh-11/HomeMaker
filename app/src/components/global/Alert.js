import { useAlert } from '../../context/AlertContext';
import Alert from '@mui/material/Alert';

const AlertDisplay = () => {
  const { alert } = useAlert();

  if (!alert) return null;
  return (
    <Alert severity={alert.severity} sx={{ position: 'fixed', top: 20, right: 20, zIndex: 9999 }}>
      {alert.message}
    </Alert>
  );
};

export default AlertDisplay;
