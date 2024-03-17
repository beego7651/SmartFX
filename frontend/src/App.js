import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('https://financialmodelingprep.com/api/v3/economic_calendar')
    .then(response => setData(response.data))
    .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>My App</h1>
    </div>
  );
};

export default App;