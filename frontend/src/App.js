import React, { useEffect } from 'react'
import axios from 'axios'

const App = () => {
  useEffect(() => {
    axios.get('/api/v1/users')
  }, [])
  return (
    <div>
      <h1>Hello!</h1>
    </div>
  )
}

export { App }
