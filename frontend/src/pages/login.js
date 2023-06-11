import { setToken,fetchToken } from "../utils/privateroute";
import { useNavigate } from 'react-router-dom';
import React, { useState ,useEffect} from "react";
export default function Login() {
  const navigate = useNavigate()
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

useEffect(()=>{
 const auth = fetchToken().token;
   if (auth) {
    navigate("/dashboard");
  }
},[])


  const login = () => {
    if (username === "" || password === "") {
      return;
    } else {



      // user logic for get access token
      setToken("123");

      navigate("/dashboard");
    }
  };

  return (
    <>
      <div style={{ minHeight: 800, marginTop: 30 }}>
        <h1>login page</h1>
        <div style={{ marginTop: 30 }}>
          <div className="w-full max-w-xs">
            <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                  Username
                </label>
                <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
              </div>
              <div className="mb-6">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                  Password
                </label>
                <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" onChange={(e) => setPassword(e.target.value)} />
              </div>
              <div className="flex items-center justify-between">
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button" onClick={login}>
                  Sign In
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}
