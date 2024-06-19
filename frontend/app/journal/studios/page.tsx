'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'

import {Studio} from '../../classes/Studio'
import Header from '../../common/header'


const BaseURL = `http://localhost:8000`


async function getStudios() {
    const result = await fetch(
        BaseURL + '/studios',
        {method: 'GET'}
    )
   
    if (!result.ok) {
      throw new Error('Failed to fetch data')
    }
   
    const raws = await result.json()
    let studios = raws.map((item: any): Studio => {
        return new Studio(item.id, item.name)
    });
    return studios;
}


const Journal = () => {
    const ApplicationHeader = 'Журнал';
    const PageHeader = 'Список студий';
    
    const [studios, setStudios] = useState<Array<Studio>>([])
    useEffect(() => {
        const dataFetch = async () => {
            const data = await getStudios();
            setStudios(data)
        }

        dataFetch();
    }, [])

    return (
        <>
            <Header>{ApplicationHeader}</Header>
            <h2>{PageHeader}</h2>
            {/* <Table param1={23123}></Table> */}
            <div>
                <span>Название студии</span>
            </div>
            {studios.map((item) => (
                <>
                    <div>
                        <span>{item.name}</span>
                        <span>   </span>
                        <Link href={`./studios/`}>Филиалы</Link>
                        <span>   </span>
                        <Link href={`./studios/${item.id}`}>О студии</Link>
                    </div>
                </>
            ))}
            <div>
                <Link href={`./studios/creation`}>Добавить студию</Link>
            </div>
        </>
    );
}

export default Journal;
