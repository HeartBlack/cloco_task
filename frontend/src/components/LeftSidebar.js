

export default function LeftSideBar(){

    const Editdata = ()=>{


        console.log("working")
    }
    return(
        <>

        <main className="main -ml-48 flex flex-grow flex-col p-4 transition-all duration-150 ease-in md:ml-0">
          <div className="table  p-2">
            <table className=" border">
              <thead>
                <tr className="bg-gray-50 border-b">
                  <th className="border-r p-2">
                    <input type="checkbox" />
                  </th>
                  <th className="p-2 border-r cursor-pointer text-sm font-thin text-gray-500">
                    <div className="flex items-center justify-center">
                      ID

                    </div>
                  </th>
                  <th className="p-2 border-r cursor-pointer text-sm font-thin text-gray-500">
                    <div className="flex items-center justify-center">
                      Name

                    </div>
                  </th>
                  <th className="p-2 border-r cursor-pointer text-sm font-thin text-gray-500">
                    <div className="flex items-center justify-center">
                      Email

                    </div>
                  </th>
                  <th className="p-2 border-r cursor-pointer text-sm font-thin text-gray-500">
                    <div className="flex items-center justify-center">
                      Address

                    </div>
                  </th>
                  <th className="p-2 border-r cursor-pointer text-sm font-thin text-gray-500">
                    <div className="flex items-center justify-center">
                      Action

                    </div>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr className="bg-gray-100 text-center border-b text-sm text-gray-600">
                  <td className="p-2 border-r">
                    <input type="checkbox"/>
                  </td>
                  <td className="p-2 border-r">1</td>
                  <td className="p-2 border-r">John Doe</td>
                  <td className="p-2 border-r">john@gmail.com</td>
                  <td className="p-2 border-r">Sydney, Australia</td>
                  <td>
                    <button onClick={Editdata} className="bg-blue-500 p-2 text-white hover:shadow-lg text-xs font-thin">Edit</button>
                    <a href ="facebook.com" className="bg-red-500 p-2 text-white hover:shadow-lg text-xs font-thin">Remove</a>
                  </td>
                </tr>

              </tbody>
            </table>
          </div>

        </main>
        </>

    )
}
