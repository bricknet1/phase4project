import Menu from 'react-burger-menu/lib/menus/slide'
import { useHistory, NavLink } from 'react-router-dom'

function NavBar({ user, setUser }){

    const history = useHistory()

    const handleLogout = () => {
        fetch('/logout', {
            method: "DELETE"
        })
        .then(res => {
            if(res.ok){
                setUser(null)
                history.push('/')
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
            <Menu right width={'15%'}>
                <NavLink id="home" className="menu-item" exact to="/">Home</NavLink>
                {user ? 
                    <>
                        <NavLink id="logout" className="bm-item" to="/login" onClick={handleLogout}>Logout</NavLink>
                        <br />
                        <NavLink id="my-profile" className="bm-item" to={`/profile/${user.id}`}>My Profile</NavLink>
                        <br />
                        <NavLink id="make-post" className="bm-item" to="/newpost">Make a Post</NavLink>
                        {user.is_admin ? 
                            <>
                                <br />
                                <NavLink id="edit-crimes" className="bm-item" to="/crimes" >Edit Crimes</NavLink> 
                            </>
                        : null}
                    </>
                    : <NavLink id="login" className="bm-item" to="/login">Login</NavLink>
                    
                }
                
            </Menu>
        </div>
    );
}

export default NavBar