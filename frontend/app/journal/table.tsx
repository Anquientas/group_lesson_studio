import { useEffect, useState } from 'react'

import {Studio} from '../classes/Studio'

import styled from 'styled-components'

async function getData() {
    const id = 9;
    const res = await fetch(
        `http://localhost:8000/studios/${id}/`,
        {
            method: 'GET',
            // body: JSON.stringify(data)
        }
    )
    // The return value is *not* serialized
    // You can return Date, Map, Set, etc.
   
    if (!res.ok) {
      // This will activate the closest `error.js` Error Boundary
      throw new Error('Failed to fetch data')
    }
   
    const raw = await res.json()
    console.log('raw', raw)
    return new Studio(raw.id, raw.name);
  }



const Table = () => {

    const [studio, setStudio] = useState<Studio|null>(null)
    useEffect(() => {
        const dataFetch = async () => {
            const data = await getData();
            setStudio(data)
            console.log('set')
        }

        if (studio == null) {
            dataFetch()
        }
        return () => {console.log('dead', studio)};
    }, [])

    console.log(studio, 'studio')
    if (studio == null) {
        return null;
    }
    return (
        <>
            <div>{studio.name}</div>
            <div>{studio.id}</div>
            {/* {studio ? <></> : <></>} */}
        </>
    );

}

export default Table;