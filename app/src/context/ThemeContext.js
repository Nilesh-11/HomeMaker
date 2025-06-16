// src/context/ThemeContext.js
import React, { createContext, useEffect, useMemo, useState } from 'react';
import { ThemeProvider as MuiThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import useMediaQuery from '@mui/material/useMediaQuery';
import { create } from 'jss';
import rtl from 'jss-rtl';
import { StylesProvider, jssPreset } from '@mui/styles';

export const ThemeContext = createContext();

const jss = create({ plugins: [...jssPreset().plugins, rtl()] });

const getInitialTheme = () => {
  return localStorage.getItem('app-theme') || 'system';
};

export const ThemeProvider = ({ children }) => {
  const systemPrefersDark = useMediaQuery('(prefers-color-scheme: dark)');
  const [themeName, setThemeName] = useState(getInitialTheme);
  const [direction, setDirection] = useState('ltr');

  const actualTheme = themeName === 'system' ? (systemPrefersDark ? 'dark' : 'light') : themeName;

  useEffect(() => {
    localStorage.setItem('app-theme', themeName);
  }, [themeName]);

  const toggleTheme = () => {
    setThemeName(prev =>
      prev === 'light' ? 'dark' : prev === 'dark' ? 'system' : 'light'
    );
  };

  const muiTheme = useMemo(() => {
    return createTheme({
      palette: {
        mode: actualTheme,
        primary: {
          main: actualTheme === 'dark' ? '#90caf9' : '#1976d2',
        },
        background: {
          default: actualTheme === 'dark' ? '#121212' : '#f5f5f5',
        },
      },
      direction,
      typography: {
        fontFamily: 'Poppins, sans-serif',
      },
    });
  }, [actualTheme, direction]);

  const value = {
    themeName,
    setTheme: setThemeName,
    toggleTheme,
    systemPrefersDark,
    direction,
    setDirection,
  };

  return (
    <ThemeContext.Provider value={value}>
      <StylesProvider jss={jss}>
        <MuiThemeProvider theme={muiTheme}>
          <CssBaseline />
          {children}
        </MuiThemeProvider>
      </StylesProvider>
    </ThemeContext.Provider>
  );
}
