//import React, { Component } from 'react'
import * as React from 'react';
import { useState } from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import Kids from './Kids';

//export default class componentName extends Component {
const style = {
    width: '100%',
    maxWidth: 360,
    bgcolor: 'background.paper',
};

export default function First() {
    const [active, setActive] = useState(false)
    const handleClicked = (event) => {
        event.preventDefault();
        console.log("firstList Clicked");
        setActive(value => !value);
    }
    return (
        <div>

            <center>
                <h2> Filhos</h2>

                <List sx={style} component="nav" aria-label="mailbox folders">
                    <ListItem button onClick={handleClicked}>
                        <ListItemText primary="Filho 1" secondary="5C" />
                    </ListItem>
                    <Divider />
                    <ListItem button divider>
                        <ListItemText primary="Filho 2" secondary="8D" />
                    </ListItem>
                    <ListItem button>
                        <ListItemText primary="Filho n" secondary="Pre I" />
                    </ListItem>
                    <Divider light />
                </List>
                {
                    active ?
                        (
                            <Kids />
                        ) : (
                            <>
                            </>
                        )
                }
            </center>
        </div>
    )
}
