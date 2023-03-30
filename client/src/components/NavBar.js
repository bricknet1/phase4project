import {slide as Menu} from 'react-burger-menu'
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
                <a id="home" className="menu-item" href="/">Home</a>
                {user ? 
                    <>
                        <a id="logout" className="bm-item" href="/login" onClick={handleLogout}>Logout</a>
                        <br />
                        <a id="my-profile" className="bm-item" href={`profile/${user.id}`}>My Profile</a>
                        <br />
                        <a id="make-post" className="bm-item" href="/newpost">Make a Post</a>
                        {user.is_admin ? 
                            <>
                                <br />
                                <a id="edit-crimes" className="bm-item" href="/crimes" >Edit Crimes</a> 
                            </>
                        : null}
                    </>
                    : <a id="login" className="bm-item" href="/login">Login</a>
                    
                }
                
            </Menu>
        </div>
    );
}

export default NavBar