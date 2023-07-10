import React, { useContext } from 'react'
import { MoonIcon } from '@heroicons/react/solid'
import ThemeContext from '../context/ThemeContext';

const ThemeIcon = () => {
    const {darkMode,setDarkMode} = useContext(ThemeContext);
    const toggleDarkMode = () =>{
        setDarkMode(!darkMode);
    }
  return (
    <button className={`rounded-lg border-1 border-neutral-400 p-2 absolute right-8 lg:right-32 shadow-lg ${darkMode ? "shadow-gray-700": null}
    transition duration-300 hover:scale-125`} 
    onClick={toggleDarkMode}>
        <MoonIcon className={`h-6 w-6 cursor-pointer stroke-1 fill-yellow-400 stroke-neutral-400 ${darkMode ? "fill-yellow-400 stroke-yellow-400": "fill-none stroke-neutral-900"}`}/>
    </button>
  )
}

export default ThemeIcon