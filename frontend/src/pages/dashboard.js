import LeftSideBar from "../components/LeftSidebar";
import RideSideBar from "../components/RightSidebar";

export default function Dashboard() {
  return (
    <>
      <div className="flex min-h-screen flex-row bg-gray-100 text-gray-800">
       <RideSideBar/>
       <LeftSideBar/>

      </div>

    </>
  )
}
