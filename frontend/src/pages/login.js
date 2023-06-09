import { setToken,fetchToken } from "../utils/privateroute";
import  { useState } from "react";
export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = () => {
    if ((username === "") & (password === "")) {
      return;
    } else {
      setToken("123");
    }

    console.log(username,password)
  };

  return (
    <>
      <div style={{ minHeight: 800, marginTop: 30 }}>
        <h1>login page</h1>
        <div style={{ marginTop: 30 }}>
          {fetchToken() ? (
            <p>you are logged in</p>
          ) : (
            <div>
              <form>
                <label style={{ marginRight: 10 }}>Input Username</label>
                <input
                  type="text"
                  onChange={(e) => setUsername(e.target.value)}
                />

                <label style={{ marginRight: 10 }}>Input Password</label>
                <input
                  type="text"
                  onChange={(e) => setPassword(e.target.value)}
                />

                <button onClick={login}>Login</button>
              </form>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
