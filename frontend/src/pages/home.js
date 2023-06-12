import React from 'react'

const Home = () => {
  return (
    <nav class="font-sans flex flex-col text-center sm:flex-row sm:text-left sm:justify-between py-4 px-6 bg-white shadow sm:items-baseline w-full">
      <div class="mb-2 sm:mb-0">
        <a href="/home" class="text-2xl no-underline text-grey-darkest hover:text-blue-dark">Home</a>
      </div>
      <div>
      <a href="/two" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Dashboard</a>
        <a href="/one" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Login</a>
        <a href="/three" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Sign Up</a>
        <a href="/three" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Logout</a>
      </div>
    </nav>
  )
}

export default Home
