import Menu from 'react-burger-menu/lib/menus/slide'
import { useHistory, NavLink } from 'react-router-dom'
import { useState } from 'react';

function NavBar({ user, setUser }){

    const history = useHistory()

    const [menuOpen, setMenuOpen] = useState(false);

    const handleClickMenuItem = () => {
        setMenuOpen(false);
    };

    const handleStateChange = (state) => {
        setMenuOpen(state.isOpen)
    };

    const handleLogout = () => {
        fetch('/logout', {
            method: "DELETE"
        })
        .then(res => {
            if(res.ok){
                setUser(null)
            }
        })
    };

    const handleClickProfile = () => {
        history.push(`/profile/${user.id}`)
    };

    return(
        <div className='navbar-container'>
            <a className="logo" href='/'>Slammr</a>
            {user ? 
                <img 
                    src={user.photo}      
                    alt={user.name} 
                    className="profile-photo-nav"
                    onClick={handleClickProfile}
                /> 
            : null}
            <Menu 
                right 
                width={'250px'} 
                isOpen={menuOpen} 
                onStateChange={handleStateChange}
            >
                <NavLink 
                    id="home" 
                    className="menu-item" 
                    exact 
                    to="/" 
                    onClick={handleClickMenuItem}
                >Home</NavLink>
                {user ? 
                    <>
                        <NavLink 
                            id="my-profile" 
                            className="bm-item" 
                            to={`/profile/${user.id}`}
                            onClick={handleClickMenuItem}
                        >My Profile</NavLink>
                        <br />
                        <NavLink 
                            id="make-post" 
                            className="bm-item" 
                            to="/newpost"
                            onClick={handleClickMenuItem}
                        >Make a New Post</NavLink>
                        {user.is_admin ? 
                            <>
                                <br />
                                <NavLink 
                                    id="edit-crimes" 
                                    className="bm-item" 
                                    to="/crimes"
                                    onClick={handleClickMenuItem} 
                                >Edit All Crimes (admin)</NavLink> 
                            </>
                        : null}
                        <NavLink 
                            id="logout" 
                            className="bm-item" 
                            to="/login" 
                            onClick={() => {
                                handleClickMenuItem();
                                handleLogout();
                            }}
                        >Logout</NavLink>
                        <br />
                    </>
                    : 
                    <NavLink 
                        id="login" 
                        className="bm-item" 
                        to="/login"
                        onClick={handleClickMenuItem}
                    >Login</NavLink>
                    
                }
                
            </Menu>
        </div>
    );
}

export default NavBar