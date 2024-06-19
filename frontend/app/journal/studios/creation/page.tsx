'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'

import {Studio} from '../../../classes/Studio'
import Header from '../../../common/header'


const BaseURL = `http://localhost:8000`


async function createStudio() {
    const result = await fetch(
        BaseURL + '/studios',
        {method: 'POST'}
    )
   
    if (!result.ok) {
      throw new Error('Failed to fetch data')
    }
   
    return result;
}


const Journal = () => {
    const ApplicationHeader = 'Журнал';
    const PageHeader = 'Добавление студии';
    
    return (
        <>
            <Header>{ApplicationHeader}</Header>
            <h2>{PageHeader}</h2>
            <div>
                <input>Введите название студии:</input>
            </div>
            <div>
                <Link href={`./`}>Назад</Link>
            </div>
        </>
    );
}

export default Journal;
