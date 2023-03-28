import {fallDown as Menu} from 'react-burger-menu'
import burgericon from '../assets/menuicon.png'
import {NavLink} from 'react-router-dom';
import { useHistory } from 'react-router-dom'

function NavBar({ user, setUser }){

    const history = useHistory()

    const handleLogout = () => {
        fetch('/logout', {
            method: "DELETE"
        })
        .then(res => {
            if(res.ok){
                setUser(null)
                history.push('/home')
            }
        })
    }

    return(
        <>
            <h1>Temporary placeholder name of app</h1>
            <Menu>
                <a id="home" className="menu-item" href="/home">Home</a>
                {user ? 
                    <a id="logout" className="menu-item" href="/logout" onClick={handleLogout}>Logout</a>
                    :
                    <a id="login" className="menu-item" href="/login">Login</a>
                }
                {/* <a id="logout" className="menu-item" href="/logout" onClick={handleLogout}>Logout</a>
                <a id="login" className="menu-item" href="/login">Login</a> */}
                <a id="make-post" className="menu-item" href="/newpost">Make a Post</a>
                <a id="edit-crimes" className="menu-item" href="/crimes" >Edit Crimes</a>
            </Menu>
        </>
    );
}

export default NavBar