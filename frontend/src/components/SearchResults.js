import React, { useContext } from 'react'
import ThemeContext from '../context/ThemeContext';
import StockContext from '../context/StockContext';

const SearchResults = ({ results }) => {
  const { darkMode } = useContext(ThemeContext);
  const { setStockSymbol } = useContext(StockContext);

  return (
    <ul className={`absolute top-12 border-2 w-full rounded-md h-64 overflow-y-scroll custom-scrollbar ${darkMode ? "bg-gray-800 border-neutral-900" : "bg-white border-neutral-200"}`}>
      {results.map((item) => {
        return <li key={item.symbol} className={`cursor-pointer p-4 m-2 flex item-center justify-between rounded-md hover:bg-indigo-200 ${darkMode ? "hover:bg-indigo-800" : null}`}
        onClick = {() => {
          setStockSymbol(item.symbol)
        }}>
          <span>{item.symbol}</span>
          <span>{item.description.toUpperCase()}</span>
        </li>
      })}
    </ul>
  )
}

export default SearchResults