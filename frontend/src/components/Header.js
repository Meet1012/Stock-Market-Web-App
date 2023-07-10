import React from 'react'
import Search from './Search'
import ThemeIcon from './ThemeIcon'

const Header = ({name}) => {
    if(name==undefined){
        name = "Dummy name"
    }
    return (
        <>
            <div className="xl:px-32">
                <h1 className="text-5xl">{name}</h1>
                <Search />
            </div>
            <ThemeIcon/>
        </>
    )
}

export default Header