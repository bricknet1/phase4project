import { Route, Switch } from 'react-router-dom'
import {useEffect, useState} from 'react'

import Home from './Home.js';
import Login from './Login.js';
import Profile from './Profile.js';
import NavBar from './NavBar.js';
import NewPost from './NewPost.js';
import Crimes from './Crimes.js';
import EditCrime from './EditCrime.js';


function App() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        fetchUser()
    },[])

    const fetchUser = () => (
        fetch('/authorized')
        .then(res => {
            if(res.ok){
            res.json()
            .then(data => {
                setUser(data)
            })
            } else {
            setUser(null)
            }
        })
    )

    return (
        <>
            <NavBar user={user} setUser={setUser}></NavBar>
            <Switch>
                <Route path="/login">
                    <Login setUser={setUser}/>
                </Route>
                <Route path="/home">
                    <Home />
                </Route>
                <Route path="/profile/:id" >
                    <Profile user={user}/>
                </Route>
                <Route path="/newpost" >
                    <NewPost />
                </Route>
                <Route path="/crimes/:id" exact>
                    <EditCrime user={user}/>
                </Route>
                <Route path="/crimes" exact>
                    <Crimes user={user}/>
                </Route>
            </Switch>  
        </>
    );
}


export default App