// src/ThemeToggler.js
import React, { useContext } from 'react';
import { ThemeContext } from '../../context/ThemeContext';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

export default function ThemeToggler() {
  const { themeName, toggleTheme, direction, setDirection } = useContext(ThemeContext);

  return (
    <Stack spacing={2}>
      <Button variant="contained" onClick={toggleTheme}>
        Toggle Theme (Current: {themeName})
      </Button>
      <Button
        variant="outlined"
        onClick={() => setDirection(direction === 'ltr' ? 'rtl' : 'ltr')}
      >
        Switch Direction (Current: {direction})
      </Button>
    </Stack>
  );
}
