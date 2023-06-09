import { Outlet, Navigate } from 'react-router-dom'
export const setToken = (token) => {
    localStorage.setItem('accecss_token', token)// make up your own token
}

export const fetchToken = (token) => {
    var auth_data = localStorage.getItem('accecss_token')
    if (auth_data != null) {
        return {'token':true}
    }
    else {
        return {'token':false}
    }
}
function PrivateRoutes() {

    let auth = fetchToken()
    // console.log(auth)
    // let auth = {'token':true}
    console.log(auth)

    return (
        auth.token ? <Outlet /> : <Navigate to="/login" />
    )
}
export default PrivateRoutes
