import React ,{useEffect}from 'react'

function App() {
  const APIURL = 'https://jsonplaceholder.typicode.com/posts';
  const handleApi = async ()=>{
    const result = await fetch(APIURL)
    const data  =await result.json()
    console.log(data)
  }
  useEffect(()=>{
    handleApi()
  },[])
  return (
    <div>App</div>
  )
}

export default App