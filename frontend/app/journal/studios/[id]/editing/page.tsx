'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'

import {Studio} from '../../../../classes/Studio'
import Header from '../../../../common/header'


const BaseURL = `http://localhost:8000`


async function changeStudio(studio_id: number) {
    const result = await fetch(
        BaseURL + `/studios/${studio_id}`,
        {method: 'POST'}
    )
   
    if (!result.ok) {
      throw new Error('Failed to fetch data')
    }
   
    return result;
}


const Journal = () => {
    const ApplicationHeader = 'Журнал';
    const PageHeader = 'Изменение данных студии';
    
    return (
        <>
            <Header>{ApplicationHeader}</Header>
            <h2>{PageHeader}</h2>
            <div>
                <input>Введите новое название студии:</input>
            </div>
            <div>
                <Link href={`./`}>Назад</Link>
            </div>
        </>
    );
}

export default Journal;
