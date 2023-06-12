import React from 'react'
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <nav class="font-sans flex flex-col text-center sm:flex-row sm:text-left sm:justify-between py-4 px-6 bg-white shadow sm:items-baseline w-full">
      <div class="mb-2 sm:mb-0">
        <Link to="/" class="text-2xl no-underline text-grey-darkest hover:text-blue-dark">Home</Link>
      </div>
      <div>
      <Link to="/dashboard" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Dashboard</Link>
        <Link to="/login" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Login</Link>
        <Link to="/signup" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Sign Up</Link>
        <Link to="/logout" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Logout</Link>
      </div>
    </nav>
  )
}

export default Home
