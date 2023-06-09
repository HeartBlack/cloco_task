import { fetchToken } from "../utils/privateroute";
import  { useState } from "react";
export default function Signup() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password1, setPassword1] = useState("");

  const signup = () => {
    if ((username === "") & (password === "")) {
      return;
    } else {
      // make api call to our backend. we'll leave this for later
    }

    console.log(username,password)
  };

  return (
    <>
      <div style={{ minHeight: 800, marginTop: 30 }}>
        <h1>Signup page</h1>
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

                <label style={{ marginRight: 10 }}>Input Email</label>
                <input
                  type="text"
                  onChange={(e) => setEmail(e.target.value)}
                />
                 <label style={{ marginRight: 10 }}>Input Password</label>
                <input
                  type="password"
                  onChange={(e) => setPassword(e.target.value)}
                />

                <label style={{ marginRight: 10 }}>Input Password 1</label>
                <input
                  type="password"
                  onChange={(e) => setPassword1(e.target.value)}
                />

                <button onClick={signup}>Login</button>
              </form>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
