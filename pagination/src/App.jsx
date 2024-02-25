import React, { useEffect, useState } from 'react'

function App() {
  const [Data, SetData] = useState([]);
  const [currentPage, SetcurrentPage] = useState(1);
  const [totalPage, setTotalpage] = useState(0);

  const APIURL = 'https://jsonplaceholder.typicode.com/posts';
  const handleApi = async () => {
    const result = await fetch(APIURL)
    const data = await result.json()
    SetData(data)
    setTotalpage(Math.ceil(data.length / 10))
    console.log(Math.ceil(data.length / 8))
    console.log(data)
  }
  useEffect(() => {
    handleApi()
  }, [])

  const handlePageChange = (newpage) => {
    SetcurrentPage(newpage)
  }

  const handleNextClick = () => {
    if (currentPage < totalPage) {
      SetcurrentPage(currentPage + 1)
    }
  }
  const handlePrevClick = () => {
    if (currentPage > 1) {
      SetcurrentPage(currentPage - 1)
    }
  }
  const preDisabled = currentPage === 1;
  const nextDisabled = currentPage === totalPage;

  const itemsPerPage = 10;
  const StartIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = StartIndex + itemsPerPage
  const itemsTodisplay = Data.slice(StartIndex, endIndex)
  return (
    <>
      <div>App</div>
      {
        itemsTodisplay && itemsTodisplay.length > 0 ? itemsTodisplay.map((el, i) => { return <li key={i}>{el.title}</li> }) : ""
      }
      {
        Array.from({ length: totalPage }, (_, i) => {
          return (
            <button className='border m-1 p-2' key={i}
              disabled={i + 1 === currentPage}
              onClick={() => handlePageChange(i + 1)}>
              {i + 1}
            </button>
          )
        })

      }

      <button onClick={handlePrevClick} className='border p-1 m-1'
        disabled={preDisabled}>Prev</button>
      <button onClick={handleNextClick}
        className='border p-1 m-1'
        disabled={nextDisabled}>next</button>

    </>


  )
}

export default App