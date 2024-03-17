import React from 'react';
import App from './App';
import { render } from 'react-dom';

const root = document.getElementById('root');
render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  root
);