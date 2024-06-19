'use client'
import { useEffect, useState } from 'react'
import { useParams } from 'next/navigation'
import Link from 'next/link'

import {Studio} from '../../../classes/Studio'
import Header from '../../../common/header'


const BaseURL = `http://localhost:8000`


async function getStudio(studio_id: number) {
    const result = await fetch(
        BaseURL + `/studios/${studio_id}`,
        {method: 'GET'}
    )
   
    if (!result.ok) {
      throw new Error('Failed to fetch data')
    }
   
    const raw = await result.json()
    return new Studio(raw.id, raw.name);
}


const Journal = () => {
    const ApplicationHeader = 'Журнал';
    const PageHeader = 'Сведения о студии';
    const params = useParams<{ id: string }>()
    const [studio, setStudio] = useState<Studio|null>(null)
    useEffect(() => {
        const dataFetch = async () => {
            const data = await getStudio(parseInt(params.id));
            setStudio(data)
        }

        if (studio == null) {
            dataFetch()
        };
    }, [])

    if (studio == null) {
        return null;
    }

    return (
        <>
            <Header>{ApplicationHeader}</Header>
            <h2>{PageHeader}</h2>
            <div>
                <span>Название: </span>
                <span>{studio.name}</span>
            </div>
            <div>
                <span>Действия: </span>
                <Link href={`./`}>Редактировать</Link>
                <span>   </span>
                <Link href={`./`}>Удалить</Link>
            </div>
            <div>
                <Link href={`./`}>Назад</Link>
            </div>
        </>
    );
}

export default Journal;
