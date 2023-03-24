import { Route, Switch, useHistory } from 'react-router-dom'
import {createGlobalStyle} from 'styled-components'
import {useEffect, useState} from 'react'


function App() {
    return (
        <>
            <Switch>
                <Route path="/login">
                    Login
                </Route>
                <Route path="/home">
                    Home
                </Route>
                <Route path="/profile/:id">
                    Profile by ID
                </Route>
            </Switch>  
        </>
    );
}


export default App