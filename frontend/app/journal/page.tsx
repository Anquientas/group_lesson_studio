'use client'
import { createContext, useEffect, useState } from 'react'

import {Studio} from '../classes/Studio'

import styled from 'styled-components'
import Table from './table'

const Context = createContext()

const Header = styled.h1`
    font-size: 24px;
    font-weight: 500px;
`;


const Journal = () => {

    const header = 'it\'s a journal bitch!';
    return (
        <>
            <Header>{header}</Header>
            <Table></Table>
        </>
    );

}

export default Journal;