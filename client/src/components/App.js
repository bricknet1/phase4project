import { Route, Switch, useHistory } from 'react-router-dom'
import {createGlobalStyle} from 'styled-components'
import {useEffect, useState} from 'react'

import Home from './Home.js';
import Login from './Login.js';
import Profile from './Profile.js';


function App() {
    const [user, setUser] = useState(null);

    return (
        <>
            <Switch>
                <Route path="/login">
                    <Login setUser={setUser}/>
                </Route>
                <Route path="/home">
                    <Home />
                </Route>
                <Route path="/profile/:id">
                    <Profile />
                </Route>
            </Switch>  
        </>
    );
}


export default App