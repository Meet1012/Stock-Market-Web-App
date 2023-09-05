import React from 'react'
import Search from './Search'
import ThemeIcon from './ThemeIcon'
import Switch from './Switch'

const Header = ({ name }) => {
    if (name == undefined) {
        name = "Dummy name"
    }
    return (
        <>
            <div className="xl:px-32">
                <h1 className="text-5xl">{name}</h1>
                <div className="flex flex-row gap-14">
                    <Search />
                    <Switch />
                </div>
            </div>
            <ThemeIcon />
        </>
    )
}

export default Header