import {fallDown as Menu} from 'react-burger-menu'
import burgericon from '../assets/menuicon.png'
import {NavLink} from 'react-router-dom';
import { useHistory } from 'react-router-dom'

function NavBar({setUser}){

    const history = useHistory()

    const handleLogout = () => {
        fetch('/logout', {
            method: "DELETE"
        })
        .then(res => {
            if(res.ok){
                setUser(null)
                history.push('/login')
            }
        })
    }

    return(
        <>
            <h1>Temporary placeholder name of app</h1>
            {/* <img src={burgericon}></img> */}
            <div id="outer-container">
                <Menu 
                //   outerContainerId={ "outer-container" } 
                //   customBurgerIcon={burgericon}
                >
                    <a id="home" className="menu-item" href="/home">Home</a>
                    <a id="logout" className="menu-item" href="/logout">Logout</a>
                    <a id="login" className="menu-item" href="/login">Login</a>
                    <a id="login" className="menu-item" href="/newpost">Make a Post</a>
                    <a id="login" className="menu-item" href="/crimes">Edit Crimes</a>
                </Menu>
            </div>
        {/* <p onClick={handleLogout}>Logout</p> */}
        {/* <NavLink to=''/> */}
        {/* <div id='outer-container' className='burger'>
            <Menu customBurgerIcon={<img src={burgericon} alt="Burger Menu Icon" />} right outerContainerId={'outer-container'} height={'50px'}>
                <a id="logout" className="menu-item" href="/logout">Logout</a>
            </Menu>
        </div> */}
        </>
    );
}

export default NavBar