import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import SignIn from "./pages/SignIn";
import FirstPage from "./pages/FirstPage/FirstPage"
import PageTeste from './pages/PageTeste/PageTeste'
const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element = {<SignIn/>} path="/" exact />
                <Route element = {<FirstPage/>} path="/firstpage" exact />
                <Route element = {<PageTeste/>} path="/user" exact />
            </Routes>        
        </BrowserRouter>
    )
}

export default AppRoutes;