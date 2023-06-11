import { Outlet, Navigate } from 'react-router-dom'
export const setToken = (token) => {
    localStorage.setItem('accecss_token', token)
}

export const fetchToken = (token) => {
    var auth_data = localStorage.getItem('accecss_token')
    console.log(auth_data)
    if (auth_data != null) {
        return {'token':true}
    }
    else {
        return {'token':false}
    }
}
function PrivateRoutes() {

    let auth = fetchToken().token

    return (
        auth ? <Outlet /> : <Navigate to="/login" />
    )
}
export default PrivateRoutes
