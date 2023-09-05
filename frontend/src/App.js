import { useState } from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import ThemeContext from './context/ThemeContext';
import StockContext from './context/StockContext';
import SwitchContext from './context/SwitchContext';

function App() {
  const [darkMode, setDarkMode] = useState(true);
  const [stockSymbol, setStockSymbol] = useState('AAPL');
  const [isSelected, setSelected] = useState(false);

  return (
    <SwitchContext.Provider value={{ isSelected, setSelected }}>
      <ThemeContext.Provider value={{ darkMode, setDarkMode }}>
        <StockContext.Provider value={{ stockSymbol, setStockSymbol }}>
          <Dashboard />
        </StockContext.Provider>
      </ThemeContext.Provider>
    </SwitchContext.Provider>
  );
}

export default App;
