import { Route, Switch, useHistory } from 'react-router-dom'
import {createGlobalStyle} from 'styled-components'
import {useEffect, useState} from 'react'

import Home from './Home.js';
import Login from './Login.js';
import Profile from './Profile.js';
import NavBar from './NavBar.js';


function App() {
    const [user, setUser] = useState(null);

    return (
        <>
            <NavBar setUser={setUser}></NavBar>
            <Switch>
                <Route path="/login">
                    <Login setUser={setUser}/>
                </Route>
                <Route path="/home">
                    <Home />
                </Route>
                <Route path="/profile/:id" user={user}>
                    <Profile />
                </Route>
            </Switch>  
        </>
    );
}


export default App