import { Route, Switch, useHistory } from 'react-router-dom'
import {createGlobalStyle} from 'styled-components'
import {useEffect, useState} from 'react'

import Home from './Home.js';
import Login from './Login.js';
import Profile from './Profile.js';


function App() {
    return (
        <>
            <Switch>
                <Route path="/login">
                    <Login />
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