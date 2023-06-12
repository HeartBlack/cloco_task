import LeftSideBar from "../components/LeftSidebar";
import RideSideBar from "../components/RightSidebar";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
export default function Dashboard() {

  const [fetchedData, setFetchedData] = useState("");

  useEffect(() => {
    getAllSongs()
  }, []);

  const getAllSongs = () => {
    axios.get('http://localhost:8000/api/v1/songs/get_all_songs/?page=1&page_size=10')
      .then(response => {
        // console.log(response.data.items)
        setFetchedData(response.data);

      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  };
  return (
    <>
      <div className="flex min-h-screen flex-row bg-gray-100 text-gray-800">
        <RideSideBar />
        <LeftSideBar data={fetchedData.items} />

      </div>

    </>
  )
}
