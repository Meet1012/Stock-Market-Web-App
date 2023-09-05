import React, { useContext } from 'react'
import ThemeContext from '../context/ThemeContext';
import SwitchContext from '../context/SwitchContext';

const Switch = () => {

    const { isSelected, setSelected } = useContext(SwitchContext);
    const { darkMode } = useContext(ThemeContext);
    return (
        <div className={`w-14 h-7 mt-7 rounded-full bg-gray-400 flex hover:scale-105 ${isSelected && darkMode ? "bg-indigo-500" : isSelected && !darkMode ? "bg-indigo-300" : "bg-gray-400"}`
        } onClick={() => setSelected(!isSelected)}>
            <span className={`w-5 mt-1 ml-1 h-5 bg-white rounded-full duration-500 ${isSelected ? "ml-8" : "ml-1"}`}>
            </span>
        </div >
    )
}

export default Switch;