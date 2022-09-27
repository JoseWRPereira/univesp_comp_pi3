import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import SignIn from "./pages/SignIn";
import FirstPage from "./pages/FirstPage/FirstPage"

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element = {<SignIn/>} path="/" exact />
                <Route element = {<FirstPage/>} path="/firstpage" exact />
            </Routes>        
        </BrowserRouter>
    )
}

export default AppRoutes;